---
description: Quy tắc riêng cho module Bảng thanh toán (payment-management)
alwaysApply: true
---
# Module Bảng thanh toán – quy tắc

## Nguồn yêu cầu
- Đặc tả gốc duy nhất: `docs/requirements/payment-management/spec.md`
  (chép nguyên văn từ `BAITAP_TA_1-2.pdf`, mục 1–6, không sửa nội dung).
- Mã tham chiếu: User Story `US-PAY-01..05`, quy tắc `PAY-01..08`, NFR ghi theo mục 6.

## Không tự suy diễn
- Chỉ dùng thông tin có trong đặc tả. Mọi chỗ mâu thuẫn, mơ hồ hoặc thiếu
  phải ghi vào bảng **Open Questions** với: vị trí (mục / mã US / mã PAY),
  loại vấn đề (Mâu thuẫn | Mơ hồ | Thiếu), mô tả, lý do cần xác nhận.
- Không chọn giúp người dùng một cách hiểu. Nếu buộc phải giả định để tiếp tục
  thiết kế, đánh dấu `[GIẢ ĐỊNH – Cần xác nhận]` và liên kết tới câu hỏi tương ứng.
- Không thêm trạng thái, vai trò, ngưỡng tiền, hay quy tắc không có trong đặc tả.

## Phạm vi
- Chỉ thiết kế: lập, trình duyệt, duyệt/từ chối, điều chỉnh, hủy bảng thanh toán.
- Hợp đồng, bảng giá, sản lượng là module khác – chỉ được **đọc** qua interface,
  không thiết kế CRUD cho chúng.

## Đầu ra
- Thiết kế: `docs/design/payment-management/` theo cấu trúc trong `.agents/agents/design.md`.
- Sơ đồ PlantUML: `docs/design/payment-management/diagrams/`.
- Tên trạng thái, tên class, tên endpoint phải giống nhau giữa mọi tài liệu và sơ đồ.
- Mỗi US-PAY, PAY và NFR phải xuất hiện trong `06-traceability-matrix.md`.
- Nhận xét review: `docs/review/payment-management/`.
