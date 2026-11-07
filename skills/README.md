# Skill quy trình – Bảng thanh toán TA 1–2

Các skill là hướng dẫn từng bước cho một loại sản phẩm, dùng chung cho mọi công cụ
AI (Claude, Codex, Cursor…). Skill **không thay** [AGENTS.md](../AGENTS.md): luôn
đọc AGENTS.md trước; nếu skill và AGENTS.md khác nhau thì AGENTS.md thắng.
Mọi skill dùng [ngữ cảnh chung](_shared/payment-context.md) (nguồn, ID, mâu thuẫn
đã biết, ảnh chụp AS-IS, quy ước mã và tên, cách kiểm tra PlantUML).

| Skill | Vai trò | Đầu ra | Thứ tự gợi ý |
|---|---|---|---|
| [sys-spec](sys-spec/SKILL.md) | ba | `docs/analysis/payment-management/sys-pay-0N-<slug>.md` | 1 |
| [uml-diagrams](uml-diagrams/SKILL.md) | design | `diagrams/class.puml`, `state-machine.puml`, `component.puml` (+ tùy chọn) | 2 |
| [sequence-diagram](sequence-diagram/SKILL.md) | design | `diagrams/sequence-<nn>-<thao-tac>.puml` + danh mục trong `03` | 3 |
| [data-design](data-design/SKILL.md) | design | `05-data-design.md` (+ `diagrams/erd.puml`) | 4 |
| [traceability-matrix](traceability-matrix/SKILL.md) | design | `06-traceability-matrix.md` | cuối |

Đường dẫn `diagrams/`, `03`, `05`, `06` nằm trong `docs/design/payment-management/`.
Skill design không viết thay 01/02/04/07/08; nếu cần dữ kiện từ đó mà chưa có thì ghi
"Chưa có <file>" và nêu trong bàn giao.

## Cách gọi

```text
Đọc AGENTS.md, đóng vai agent <ba|design> và dùng skill <tên> trong
skills/<tên>/SKILL.md cho <phạm vi, vd. US-PAY-02>. Đọc skills/_shared/payment-context.md.
Nêu nguồn đã đọc, file sẽ ghi và phần Blocked by OQ trước khi làm.
```

Ví dụ:

```text
Đọc AGENTS.md, đóng vai agent ba, dùng skill sys-spec cho US-PAY-02.
```

```text
Đọc AGENTS.md, đóng vai agent design, dùng skill sequence-diagram cho thao tác
submit và approve. Giữ OQ-P03-01/02 ở trạng thái Cần xác nhận.
```

Skill không cấp quyền phê duyệt nghiệp vụ, không cho sửa `src/`, đặc tả hay báo
cáo reviewer. Reviewer không có skill riêng ở đây; dùng vai trò reviewer trong
AGENTS.md ở chat mới. Ghi mỗi lần chạy vào
[prompt-log](../docs/workflow/prompt-log.md).
