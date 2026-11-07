#!/usr/bin/env python3
"""Verify the shared AGENTS.md and sources; --codex also checks the real loader."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PDF_SHA256 = "bc8b34cc847343151a496c2a515a7178bf90a834d5bee909bddcf56179bd218e"
SPEC_SHA256 = "7fc1f7f54d291a3ea442d5475fce6fd660ed15919fdc49717f8db00c2e3ac951"
LEGACY_PATHS = (".agents", ".codex", ".claude", ".cursor", "CLAUDE.md",
                "scripts/sync_agent_config.py")


def text_values(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "text" and isinstance(child, str):
                yield child
            else:
                yield from text_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from text_values(child)


def verify(codex=False):
    failures = []

    def check(condition, label):
        print(f"{'PASS' if condition else 'FAIL'}: {label}")
        if not condition:
            failures.append(label)

    guidance = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for heading in ("Nguồn yêu cầu", "Quy tắc chung", "Phạm vi Bảng thanh toán",
                    "Vai trò ba", "Vai trò design", "Vai trò reviewer",
                    "Bàn giao và nhật ký"):
        check(guidance.splitlines().count("## " + heading) == 1,
              "shared guidance section: " + heading)
    for relative in LEGACY_PATHS:
        check(not (ROOT / relative).exists(),
              "separate configuration removed: " + relative)
        check(relative not in guidance, "no obsolete instruction reference: " + relative)

    for relative in ("README.md", "docs/workflow/README.md",
                     "docs/workflow/config-verification.md", "docs/workflow/prompt-log.md",
                     "docs/requirements/payment-management/sources.md",
                     "docs/analysis/payment-management",
                     "docs/design/payment-management/diagrams",
                     "docs/review/payment-management"):
        check((ROOT / relative).exists(), "workspace path: " + relative)
    for relative, digest in (
        ("docs/requirements/payment-management/assignment-ta-1-2.pdf", PDF_SHA256),
        ("docs/requirements/payment-management/spec.md", SPEC_SHA256),
    ):
        path = ROOT / relative
        check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
              "source preserved (SHA-256): " + relative)

    setup_docs = ["AGENTS.md", "README.md", "docs/workflow/README.md",
                  "docs/workflow/config-verification.md", "docs/workflow/prompt-log.md",
                  "docs/requirements/payment-management/sources.md",
                  "docs/design/payment-management/README.md"]
    for relative in setup_docs:
        path = ROOT / relative
        content = path.read_text(encoding="utf-8")
        missing = []
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if not (path.parent / target).exists():
                missing.append(target)
        check(not missing, "local links: " + relative +
              (f" missing {missing}" if missing else ""))

    if codex:
        executable = shutil.which("codex")
        check(bool(executable), "Codex executable available")
        if executable:
            version = subprocess.run([executable, "--version"], capture_output=True,
                                     text=True, timeout=15)
            print("INFO: " + version.stdout.strip())
            result = subprocess.run(
                [executable, "debug", "prompt-input", "Kiểm tra nạp file chung, không làm tác vụ khác."],
                cwd=ROOT, capture_output=True, text=True, timeout=60)
            check(result.returncode == 0, "Codex real prompt loader ran")
            if result.returncode:
                print("INFO: Inspect local Codex availability and terminal permissions; "
                      "raw prompts/configuration are not printed.")
            else:
                items = json.loads(result.stdout)
                project_texts = [
                    text for item in items
                    if item.get("type") == "message" and item.get("role") == "user"
                    for text in text_values(item.get("content", []))
                ]
                check(any(guidance.rstrip() in text for text in project_texts),
                      "Codex loaded complete shared AGENTS.md")
                print("INFO: Shared rules and all three role definitions checked together; "
                      "no model call or business-agent execution was performed.")
    print(f"RESULT: {'FAIL' if failures else 'PASS'} ({len(failures)} failed checks)")
    return bool(failures)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex", action="store_true",
                        help="Inspect local Codex prompt loader without a model call")
    args = parser.parse_args()
    try:
        sys.exit(verify(args.codex))
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
