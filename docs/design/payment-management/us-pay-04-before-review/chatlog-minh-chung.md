# US-PAY-04 — Chatlog và minh chứng Before Review

**Phụ trách Lộc · Module Bảng thanh toán**

Nhật ký chọn các prompt có yêu cầu cụ thể về đặc tả, cách xử lý bảng `Approved` hoặc mức chi tiết của sơ đồ. Phần trích dẫn giữ nguyên cách diễn đạt. Dấu `[…]` đánh dấu đoạn đã lược. Các liên kết minh chứng trỏ tới tài liệu đang có trong repo.

## P-01 — Đọc đề và đề xuất cách xử lý US-04

> mỗi US có  -> sys spec/  sequence / state diagram
>
> […]
>
> US-04: LỘC
>
> […]
>
> từ cái đặc tả, nó sai, mình dùng AI phân tích suy luận gì đó, rồi đưa ra các đề xuất, mỗi đề xuất kèm theo thiết kế cho hướng đề xuất đó cho khách hàng của mình

Prompt này có đính kèm `BAITAP_TA_1-2.pdf` và ảnh mẫu System Use Case. AI đối chiếu §4.4 với PAY-05 ở trang 2 và yêu cầu audit ở §6 trang 3. Điểm phát hiện là cách hiểu “điều chỉnh” thành sửa trực tiếp bảng `Approved` sẽ xung đột với PAY-05. Hai hướng đưa ra là lập hồ sơ riêng (A) và sửa trực tiếp theo ngoại lệ (B). Các phần chưa có quy tắc được ghi thành OQ-01 đến OQ-03. [Đặc tả gốc](../../../requirements/payment-management/spec.md) · [System Spec Before Review](us-pay-04-before-review.md) · [Điểm cần kiểm tra lại trong đề](us-pay-04-issues.md)

## P-02 — Kiểm tra mức chi tiết của Sequence Diagram

> Sequence Diagram của tôi chỉ ngắn gồm 1 module và 1 db vây thôi không bao gồm cái class hãy chức năng gì khác hả

Prompt chỉ ra sơ đồ tổng quan gom xử lý vào một module và một kho dữ liệu. Ở bản chi tiết, các lifeline thể hiện màn hình điều chỉnh, `PaymentAdjustmentService`, `PaymentRepository`, `AdjustmentRepository` và `AuditRepository`. Có thể đối chiếu vai trò từng thành phần qua lời gọi đọc bảng, lưu hồ sơ hoặc cập nhật bảng gốc, và ghi audit. [Sequence Diagram hai phương án](sequence.svg) · [Nguồn PlantUML](us-pay-04-before-review-sequence.puml)

## P-03 — Bám vào vướng mắc `Approved` và so sánh A/B

> dựa trên điểm không ổn ở phần approved, bám theo 2 cách đã đề xuất, xuất vào 1 folder, có sẵn ai review rồi giờ cần 1 file markdown sau review gồm  sys spec/  sequence

Hai nhánh trong sequence cho thấy khác biệt tại bước lưu. A gọi `AdjustmentRepository.Create` để lưu hồ sơ liên kết và giữ dữ liệu gốc. B kiểm tra ngoại lệ PAY-05 rồi mới gọi `PaymentRepository.UpdateApproved`. Cả hai ghi audit theo §6. Sau khi sắp xếp lại các tệp, bản đối chiếu A/B nằm trong bộ Before Review. Bản After Review hiện tại mô tả chi tiết phương án A theo [prompt P-04](../us-pay-04-after-review/chatlog-minh-chung.md). [System Spec hai phương án](us-pay-04-before-review.md) · [Sequence Diagram hai phương án](sequence.svg)
