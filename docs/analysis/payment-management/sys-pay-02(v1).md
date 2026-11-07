# US-PAY-02 – Đặc tả v1

Bản chụp nội dung bảng gốc v1 trong Google Doc do người dùng chỉ định, trước khi soạn v2. Giữ nguyên nội dung các ô; phần chú giải sau bảng không thuộc bản gốc. Trạng thái: Design Pending Approval.

| Trường | Nội dung bản gốc |
|---|---|
| Tên Use Case | US-PAY-02 – Trình duyệt bảng thanh toán.  |
| Tác nhân | Tác nhân chính: Nhân viên kinh doanh (NVKD). Người duyệt là bên nhận thông báo  |
| Mục tiêu | Trình bảng thanh toán hợp lệ để chuyển từ Draft sang PendingApproval và gửi thông báo cho người duyệt. Mỗi lần chuyển trạng thái phải có audit: ai, lúc nào, thay đổi gì.  |
| Kích hoạt | NVKD chọn chức năng “Trình duyệt” cho bảng thanh toán. |
| Tiền điều kiện | Người thực hiện là NVKD; bảng thanh toán đã được lập và đang ở Draft. <br>Các kiểm tra PAY-04 thuộc dòng xử lý, không được giả định đã đạt trước khi bắt đầu. |
| Dòng cơ bản | NVKD chọn “Trình duyệt”.<br>Hệ thống kiểm tra PAY-04: tổng tiền không âm, không thiếu dòng dịch vụ bắt buộc và chống thao tác trình duyệt trùng. <br>Nếu đạt, hệ thống chuyển Draft → PendingApproval, ghi audit người thực hiện, thời điểm và thay đổi trạng thái. <br>Hệ thống gửi thông báo duyệt cho người duyệt. <br>Hệ thống hiển thị kết quả trình duyệt và trạng thái PendingApproval.  |
| Dòng thay thế | A2.1 – Tổng tiền âm: hệ thống chặn trình duyệt. Giữ Draft, hiển thị lỗi để NVKD chỉnh sửa và thực hiện lại.<br>A2.2 – Thiếu dòng dịch vụ bắt buộc: hệ thống chặn trình duyệt. Giữ Draft, chỉ ra nội dung thiếu. <br>A2.3 – Trình duyệt trùng (bước 2–3): hệ thống chặn thao tác lặp. Không tạo thêm lần chuyển trạng thái; phản hồi trạng thái hiện tại.  |

## Nguồn và giới hạn

[ĐẶC TẢ] TA-SPEC §2–3; §4.2, US-PAY-02; §5 PAY-04; §6 audit tại [spec.md](../../requirements/payment-management/spec.md). Phân cấp người duyệt: §4.3 ↔ §5 PAY-06; cấm người lập tự duyệt: PAY-07. Chưa mở TA-PDF trong lần này.

[ĐỀ XUẤT KỸ THUẬT] Cách phản hồi giao diện/giữ trạng thái trong bảng là diễn đạt thiết kế. v1 chưa quy định giao dịch, phiên bản, phân công cụ thể hoặc cách xử lý lỗi gửi. Không coi các chi tiết v2 là đã tồn tại ở v1.

OQ-US-PAY-02-01: thiếu danh mục dịch vụ bắt buộc (PAY-04); OQ-US-PAY-02-02: người duyệt đúng 500 triệu (§4.3 ↔ PAY-06); OQ-US-PAY-02-03: kênh và tiêu chí gửi thông báo (§4.2). Các OQ giữ Cần xác nhận; bảng đầy đủ và các câu hỏi bổ sung ở [v2](sys-pay-02(v2).md).

## Bản tiếp theo

[Đặc tả v2 và sequence tương ứng](sys-pay-02(v2).md).
