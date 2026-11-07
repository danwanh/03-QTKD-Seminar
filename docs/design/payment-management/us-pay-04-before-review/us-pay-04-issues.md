# US-PAY-04 — Điểm cần kiểm tra lại trong đề

**Phụ trách Lộc · Phạm vi điều chỉnh bảng thanh toán đã duyệt**

Căn cứ đối chiếu là §1, §3, §4.4 và PAY-05 (§5) trong [đặc tả gốc](../../../requirements/payment-management/spec.md) (PDF đề bài, tr. 1–2). Các câu hỏi dưới đây liên kết với [System Spec Before Review](us-pay-04-before-review.md) và [Sequence Diagram](sequence.svg).

## Open Questions

| Mã | Vị trí trong đề | Loại | Điểm chưa hợp lý hoặc cần kiểm tra | Cần khách hàng xác nhận | Ảnh hưởng đến thiết kế |
|---|---|---|---|---|---|
| **OQ-01** | §4.4 US-PAY-04 và PAY-05 (§5) | Mâu thuẫn nếu sửa trực tiếp | §4.4 cho phép Kế toán trưởng điều chỉnh bảng `Approved` khi có biên bản, còn PAY-05 cấm sửa bảng `Approved`. Từ “điều chỉnh” chưa chỉ rõ có được sửa bảng gốc hay chỉ ghi nhận điều chỉnh riêng. | Giữ bảng gốc và lập hồ sơ điều chỉnh riêng (A), hay phê chuẩn ngoại lệ cho phép cập nhật bảng gốc (B)? | Quyết định nơi ghi thay đổi và việc có cần bổ sung ngoại lệ vào PAY-05. |
| **OQ-02** | §4.4 US-PAY-04 | Thiếu | Đề yêu cầu đính kèm biên bản xác nhận nhưng chưa nêu tiêu chí chấp nhận biên bản và phạm vi nội dung được điều chỉnh. | Hướng A cần những thông tin nào trong hồ sơ? Hướng B cho sửa trường nào? Biên bản cần đáp ứng tiêu chí gì? | Quyết định dữ liệu nhập và điều kiện hệ thống kiểm tra trước khi lưu. |
| **OQ-03** | §1, §3 và §4.4 US-PAY-04 | Thiếu | Đề yêu cầu bảng được duyệt trước khi chuyển kế toán xuất hóa đơn, nhưng chưa mô tả quy trình áp dụng số liệu đã điều chỉnh. | Có phải duyệt lại không và ai duyệt? Với B, bảng ở trạng thái nào sau khi sửa? Khi nào kế toán được dùng số mới và xử lý ra sao nếu đã phát hành hóa đơn? | Quyết định trạng thái, quy trình sau khi ghi nhận và thời điểm áp dụng số liệu. |

## Ví dụ để trao đổi về OQ-01

Giả sử bảng đã duyệt ghi **120 triệu** và biên bản xác nhận số đúng là **115 triệu**.

- **A:** Bảng gốc vẫn ghi **120 triệu** và giữ `Approved`. Hệ thống lưu hồ sơ riêng ghi **giảm 5 triệu**, liên kết với bảng gốc. Kế toán chỉ dùng số **115 triệu** khi khoản điều chỉnh được phép áp dụng theo OQ-03.
- **B:** Hệ thống cập nhật trực tiếp bảng gốc từ **120 triệu xuống 115 triệu** và lưu vết trước/sau. B chỉ thực hiện được sau khi ngoại lệ PAY-05 được phê chuẩn và yêu cầu đáp ứng điều kiện đã chốt.
