#!/usr/bin/env python3
"""Check adapters and sources; --codex also inspects Codex's real prompt loader."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tomllib

from sync_agent_config import ROOT, expected_adapters, frontmatter

PDF_SHA256 = "bc8b34cc847343151a496c2a515a7178bf90a834d5bee909bddcf56179bd218e"
SPEC_SHA256 = "7fc1f7f54d291a3ea442d5475fce6fd660ed15919fdc49717f8db00c2e3ac951"


def verify(codex=False):
    failures = []

    def check(condition, label):
        print(f"{'PASS' if condition else 'FAIL'}: {label}")
        if not condition:
            failures.append(label)

    roles = {"ba", "design", "reviewer"}
    check({p.stem for p in (ROOT / ".agents/agents").glob("*.md")} == roles,
          "canonical roles: ba, design, reviewer")
    check({"qtkd-context", "payment-management"}.issubset(
          {p.stem for p in (ROOT / ".agents/rules").glob("*.md")}),
          "both mandatory canonical rules exist")
    expected = expected_adapters()
    for relative, content in expected.items():
        path = ROOT / relative
        check(path.is_file() and path.read_text(encoding="utf-8") == content,
              f"adapter synchronized: {relative}")
    for folder, extension in ((".cursor/agents", "md"), (".claude/agents", "md"),
                              (".codex/agents", "toml"), (".cursor/rules", "mdc")):
        actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / folder).glob(f"*.{extension}")}
        wanted = {p for p in expected if p.startswith(folder + "/")}
        check(actual == wanted, f"no missing/unmanaged adapters: {folder}")

    for path in sorted((ROOT / ".cursor/rules").glob("*")):
        check(path.suffix == ".mdc", f"Cursor rule extension: {path.name}")
        if path.suffix != ".mdc":
            continue
        meta, body = frontmatter(path.read_text(encoding="utf-8"))
        check(meta.get("alwaysApply") is True and isinstance(meta.get("description"), str)
              and bool(meta["description"].strip()) and bool(body.strip()),
              f"Cursor alwaysApply/frontmatter: {path.name}")
    for path in sorted((ROOT / ".codex/agents").glob("*.toml")):
        meta = tomllib.loads(path.read_text(encoding="utf-8"))
        check(meta.get("name") in roles and all(isinstance(meta.get(k), str) and meta[k]
              for k in ("name", "description", "developer_instructions")),
              f"Codex TOML schema: {path.name}")
        check("model" not in meta and "model_reasoning_effort" not in meta,
              f"Codex inherits model settings: {path.name}")
    for folder in (".cursor/agents", ".claude/agents"):
        for path in sorted((ROOT / folder).glob("*.md")):
            meta, body = frontmatter(path.read_text(encoding="utf-8"))
            check(meta.get("name") == path.stem and meta.get("model") == "inherit"
                  and bool(meta.get("description")) and bool(body.strip()),
                  f"agent frontmatter: {folder}/{path.name}")

    entrypoint = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for path in sorted((ROOT / ".agents/rules").glob("*.md")):
        check(path.relative_to(ROOT).as_posix() in entrypoint,
              f"AGENTS.md references rule: {path.name}")
    check("@AGENTS.md" in (ROOT / "CLAUDE.md").read_text(encoding="utf-8"),
          "CLAUDE.md imports AGENTS.md")
    for relative in ("README.md", "docs/workflow/README.md",
                     "docs/workflow/config-verification.md",
                     "docs/requirements/payment-management/sources.md",
                     "docs/analysis/payment-management",
                     "docs/design/payment-management/diagrams",
                     "docs/review/payment-management"):
        check((ROOT / relative).exists(), f"workspace path: {relative}")
    for relative, digest in (
        ("docs/requirements/payment-management/assignment-ta-1-2.pdf", PDF_SHA256),
        ("docs/requirements/payment-management/spec.md", SPEC_SHA256),
    ):
        path = ROOT / relative
        check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
              f"source preserved (SHA-256): {relative}")

    # Only validate Markdown links in maintained setup docs; do not scan sources or secrets.
    setup_docs = [ROOT / "README.md", ROOT / "docs/workflow/README.md",
                  ROOT / "docs/workflow/config-verification.md",
                  ROOT / "docs/requirements/payment-management/sources.md"]
    for path in setup_docs:
        missing = []
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if not (path.parent / target).exists():
                missing.append(target)
        check(not missing, f"local links: {path.relative_to(ROOT)}" +
              (f" missing {missing}" if missing else ""))

    if codex:
        executable = shutil.which("codex")
        check(bool(executable), "Codex executable available")
        if executable:
            version = subprocess.run([executable, "--version"], capture_output=True,
                                     text=True, timeout=15)
            print("INFO: " + version.stdout.strip())
            result = subprocess.run(
                [executable, "debug", "prompt-input", "Kiểm tra nạp cấu hình, không làm tác vụ khác."],
                cwd=ROOT, capture_output=True, text=True, timeout=60)
            check(result.returncode == 0, "Codex real prompt loader ran")
            if result.returncode:
                # Do not print raw prompts/configuration that can contain private global context.
                print("INFO: Codex loader failed. Inspect terminal permissions/local Codex availability.")
            else:
                items = json.loads(result.stdout)
                raw = json.dumps(items, ensure_ascii=False)
                check("QTKD Seminar – hướng dẫn workspace TA 1–2" in raw,
                      "Codex loaded this project's AGENTS.md")
                check(all(f".agents/rules/{name}.md" in raw for name in
                          ("qtkd-context", "payment-management")),
                      "Codex received both rule references")
                # Inspect only actual tool metadata, not mentions inside AGENTS.md.
                # This shape was observed in the installed CLI's prompt-input output.
                definitions = []

                def find_agent_type(value):
                    if isinstance(value, dict):
                        properties = value.get("properties")
                        if isinstance(properties, dict) and isinstance(properties.get("agent_type"), dict):
                            definitions.append(properties["agent_type"])
                        for child in value.values():
                            find_agent_type(child)
                    elif isinstance(value, list):
                        for child in value:
                            find_agent_type(child)

                for item in items:
                    if item.get("type") == "additional_tools":
                        find_agent_type(item)
                check(bool(definitions), "Codex exposes native agent_type inventory")
                for path in sorted((ROOT / ".codex/agents").glob("*.toml")):
                    meta = tomllib.loads(path.read_text(encoding="utf-8"))
                    check(any(meta["description"] in entry.get("description", "")
                              and re.search(r"(?<![\w-])" + re.escape(meta["name"]) +
                                            r"(?![\w-])", entry.get("description", ""))
                              for entry in definitions),
                          f"Codex discovered native agent: {meta['name']}")
                print("INFO: Project guidance and native agent registration verified; "
                      "no model call or business-agent execution was performed.")
    print(f"RESULT: {'FAIL' if failures else 'PASS'} ({len(failures)} failed checks)")
    return bool(failures)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex", action="store_true", help="Run local Codex prompt loader, without a model call")
    args = parser.parse_args()
    try:
        sys.exit(verify(args.codex))
    except (OSError, ValueError, KeyError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
