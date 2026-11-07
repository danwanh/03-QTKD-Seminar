# QTKD Seminar – hướng dẫn workspace TA 1–2

## Bắt buộc trước mọi tác vụ
Đọc và tuân thủ toàn bộ .agents/rules/:
- .agents/rules/qtkd-context.md
- .agents/rules/payment-management.md

Nguồn và phạm vi: docs/requirements/payment-management/sources.md.
Đặc tả TA 1–2: docs/requirements/payment-management/spec.md.
Không tự chốt nghiệp vụ mâu thuẫn/mơ hồ/thiếu; ghi Cần xác nhận và dẫn nguồn.

## Gọi vai trò
Khi người dùng nói “đóng vai agent <tên>” hoặc “dùng agent <tên>”, đọc đúng file:

| Agent | Hướng dẫn gốc | Đầu ra được ghi |
|---|---|---|
| ba | .agents/agents/ba.md | docs/analysis/payment-management/ |
| design | .agents/agents/design.md | docs/design/payment-management/ |
| reviewer | .agents/agents/reviewer.md | docs/review/payment-management/ |

Mặc định làm vai trò trong chat hiện tại. Chỉ tạo subagent khi người dùng yêu cầu
ủy nhiệm/chạy subagent rõ ràng; không tự mở chat mới hay chạy song song.
Reviewer nên ở chat mới, đọc đặc tả và bản thiết kế độc lập.

## Cách công cụ dùng cấu hình
- Codex đọc AGENTS.md. Đổi vai trò bằng prompt bên trên luôn dùng được;
  .codex/agents/*.toml là adapter custom agent cho bản Codex hỗ trợ.
- Claude Code đọc CLAUDE.md; file đó nhập lại AGENTS.md.
  .claude/agents/*.md là adapter subagent khi công cụ hỗ trợ.
- Cursor dùng .cursor/rules/*.mdc và .cursor/agents/*.md.
- .agents/ là nguồn dùng chung, không phải thư mục tự đăng ký custom agent.
  Sau khi sửa nguồn, chạy python3 scripts/sync_agent_config.py rồi
  python3 scripts/verify_agent_config.py. Không sửa tay adapter sinh tự động.

Hướng dẫn chạy, prompt mẫu, cấu trúc và giới hạn kiểm chứng: README.md.
Quy trình lưu prompt, bản trước/sau review và phần AI/nhóm sửa:
docs/workflow/README.md. Kiểm chứng cấu hình: docs/workflow/config-verification.md.
