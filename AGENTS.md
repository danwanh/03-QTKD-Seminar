# QTKD Seminar – hướng dẫn cho AI agent (Codex & Claude)

Toàn bộ rules và agents nằm chung trong `.agents/` (tương đương `.cursor/` trong đề bài),
dùng chung cho cả Codex và Claude:

| Thư mục | Nội dung |
|---|---|
| `.agents/rules/` | Quy tắc luôn áp dụng (tương đương `.cursor/rules`) |
| `.agents/agents/` | Định nghĩa vai trò agent (tương đương `.cursor/agents`) |

Codex tự đọc `AGENTS.md`; Claude tự đọc `CLAUDE.md` (nạp lại file này).

## Bắt buộc trước mọi tác vụ
Đọc và tuân thủ toàn bộ file trong `.agents/rules/`:
- `.agents/rules/qtkd-context.md`
- `.agents/rules/payment-management.md`

## Agents
| Agent | File | Việc |
|---|---|---|
| `ba` | `.agents/agents/ba.md` | Phân tích yêu cầu |
| `design` | `.agents/agents/design.md` | Thiết kế HLD/LLD + UML |
| `reviewer` | `.agents/agents/reviewer.md` | Review thiết kế so với đặc tả |

Khi người dùng nói "đóng vai agent <tên>" (hoặc "dùng agent <tên>"), đọc file tương ứng
và làm theo đúng hướng dẫn trong đó, kể cả phần hạn chế.
Agent `reviewer` nên chạy trong phiên chat mới để review độc lập với phiên thiết kế.

## Cấu trúc liên quan bài tập Bảng thanh toán
- Đặc tả: `docs/requirements/payment-management/spec.md`
- Thiết kế: `docs/design/payment-management/` (+ `diagrams/`)
- Review AI: `docs/review/payment-management/`
