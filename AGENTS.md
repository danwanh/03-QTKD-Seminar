# QTKD Seminar – hướng dẫn cho AI agent (Codex & Claude)

Nguồn gốc duy nhất của rules và agents nằm trong `.agents/`:

| Thư mục | Nội dung |
|---|---|
| `.agents/rules/` | Quy tắc luôn áp dụng (tương đương `.cursor/rules`) |
| `.agents/agents/` | Định nghĩa vai trò agent (tương đương `.cursor/agents`) |
| `.claude/agents/` | Wrapper để Claude Code nhận subagent, trỏ về `.agents/agents/` |
| `.codex/agents/` | Wrapper để Codex nhận custom agent, trỏ về `.agents/agents/` |

## Bắt buộc trước mọi tác vụ
Đọc và tuân thủ toàn bộ file trong `.agents/rules/`:
- `.agents/rules/qtkd-context.md`
- `.agents/rules/payment-management.md`

## Agents
- `ba` – phân tích yêu cầu → `.agents/agents/ba.md`
- `design` – thiết kế HLD/LLD + UML → `.agents/agents/design.md`
- `reviewer` – review thiết kế so với đặc tả → `.agents/agents/reviewer.md`

Khi được yêu cầu đóng vai một agent, đọc file tương ứng và làm theo đúng hướng dẫn trong đó.

## Cấu trúc liên quan bài tập Bảng thanh toán
- Đặc tả: `docs/requirements/payment-management/spec.md`
- Thiết kế: `docs/design/payment-management/` (+ `diagrams/`)
- Review AI: `docs/review/payment-management/`
