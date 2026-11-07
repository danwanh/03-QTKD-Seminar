# SYS-PAY-04 — Điều chỉnh bảng thanh toán đã duyệt

**After Review · Phương án A · Phụ trách Lộc**

Bảng đã duyệt lưu số liệu tại thời điểm phê duyệt theo PAY-05 (§5). Kế toán trưởng (KTT) ghi nhận sai sót qua hồ sơ điều chỉnh riêng theo US-PAY-04 (§4.4). Màn hình nghiệp vụ và dữ liệu chuyển sang kế toán dùng cùng một kết quả xác định số tiền có hiệu lực. [Đặc tả gốc](../../../requirements/payment-management/spec.md) · [Before Review](../us-pay-04-before-review/us-pay-04-before-review.md)

## Dữ liệu và cách sử dụng

| Dữ liệu | Ví dụ | Dùng để làm gì |
| --- | --- | --- |
| Bảng thanh toán gốc | **120 triệu đồng**, trạng thái `Approved` | Tra cứu số tiền và các dòng đã duyệt ban đầu. |
| Hồ sơ điều chỉnh | **120 → 100 triệu đồng** | Liên kết với mã bảng gốc và lưu tổng tiền trước/sau, các dòng thay đổi trước/sau và biên bản xác nhận. |
| Số tiền có hiệu lực | **100 triệu đồng** khi điều chỉnh có hiệu lực | Hiển thị ở màn hình nghiệp vụ và dùng khi chuyển dữ liệu sang kế toán. Trước thời điểm đó, ví dụ này vẫn dùng **120 triệu đồng**. |

## System Spec

| Mục | Thiết kế sau review |
| --- | --- |
| Tác nhân và kích hoạt | KTT phát hiện sai sót sau khi bảng được duyệt và gửi nội dung điều chỉnh kèm biên bản. |
| Tiền điều kiện | Người thao tác có quyền KTT, bảng tồn tại và đang `Approved`, có biên bản xác nhận đính kèm. Tiêu chí chấp nhận nội dung và biên bản chờ OQ-02. |
| Dòng cơ bản | **1.** KTT gửi yêu cầu qua màn hình điều chỉnh.<br>**2.** `PaymentAdjustmentService` kiểm tra tiền điều kiện và nội dung.<br>**3.** `AdjustmentRepository` lưu hồ sơ liên kết với bảng gốc. `AuditRepository` ghi người thao tác, thời điểm và nội dung thay đổi (§6). Cả hai thao tác nằm trong cùng giao dịch.<br>**4.** Hệ thống trả kết quả đã ghi nhận hồ sơ sau khi giao dịch thành công. Bảng gốc tiếp tục ở `Approved` với số liệu đã duyệt ban đầu. |
| Dòng thay thế | Thiếu quyền, thiếu biên bản, bảng không tồn tại, bảng chưa `Approved` hoặc nội dung không đạt tiêu chí đã xác nhận thì trả lý do từ chối. Nếu ghi hồ sơ hoặc audit thất bại thì hoàn tác giao dịch và trả lỗi. |
| Tra cứu và chuyển kế toán | Khi tra cứu nghiệp vụ hoặc chuẩn bị dữ liệu cho kế toán, hệ thống lấy số tiền và các dòng từ cùng một kết quả áp dụng điều chỉnh. Nếu chưa có điều chỉnh có hiệu lực thì dùng số liệu đã duyệt. Khi hồ sơ trong ví dụ có hiệu lực, cả hai đầu sử dụng **100 triệu đồng**. Điều kiện bảng đã duyệt trước khi chuyển kế toán vẫn áp dụng theo §1. |

## Đề xuất kỹ thuật

- Dùng chung logic `ResolveEffectivePayment` cho màn hình nghiệp vụ và luồng chuẩn bị dữ liệu chuyển kế toán. Kết quả được xác định từ bảng gốc và các hồ sơ có hiệu lực tại thời điểm sử dụng. Màn hình lịch sử lấy trực tiếp số liệu đã duyệt và hồ sơ liên quan.
- Giá trị trước điều chỉnh phản ánh số liệu đang có hiệu lực khi ghi nhận hồ sơ. Ví dụ **120 → 100 triệu đồng** là lần điều chỉnh đầu tiên. Nếu cơ sở tính thay đổi trong lúc ghi nhận, hệ thống yêu cầu tải lại dữ liệu trước khi lưu hồ sơ để tránh dùng số liệu cũ.
- Phản hồi **Đã ghi nhận hồ sơ** xác nhận giao dịch lưu hồ sơ và audit. Điều kiện để áp dụng hồ sơ được xử lý riêng theo OQ-03.

## Open Questions

| Mã | Vị trí | Loại | Cần xác nhận | Ảnh hưởng |
| --- | --- | --- | --- | --- |
| OQ-02 | US-PAY-04 (§4.4) | Thiếu | Nội dung nào được phép điều chỉnh và biên bản cần đáp ứng tiêu chí gì? | Xác định phạm vi dữ liệu và điều kiện chấp nhận hồ sơ. |
| OQ-03 | §1, §3 và US-PAY-04 (§4.4) | Thiếu | Hồ sơ có cần duyệt lại không, ai duyệt, khi nào có hiệu lực và áp dụng theo thứ tự nào nếu có nhiều hồ sơ? Xử lý ra sao nếu số liệu cũ đã chuyển sang kế toán hoặc hóa đơn đã phát hành? | Xác định lúc hai luồng chuyển sang dùng số mới và cách xử lý dữ liệu đã gửi. |

OQ-01 được xử lý trong phạm vi bản thiết kế này bằng cách dùng hồ sơ riêng theo phương án A. Điều kiện hiệu lực trong sơ đồ là điểm chờ xác nhận theo OQ-03. [Các câu hỏi Before Review](../us-pay-04-before-review/us-pay-04-issues.md)

[Sơ đồ tuần tự After Review (PlantUML)](us-pay-04-after-review-sequence.puml)
