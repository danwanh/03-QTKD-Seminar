---
description: "Phạm vi và rào chắn nghiệp vụ Bảng thanh toán của bài TA 1–2"
globs: ""
alwaysApply: true
---
# Module Bảng thanh toán – TA 1–2

## Nguồn và phạm vi
- Đặc tả làm chuẩn: `docs/requirements/payment-management/spec.md` (TA-SPEC),
  bản chép §1–6 của TA-PDF, trang 1–3. Không sửa file này.
- Sổ nguồn: `docs/requirements/payment-management/sources.md`.
  `QTKD_DATH.pdf` và `BA_QTKD_User_Stories.xlsx` là bối cảnh đồ án rộng hơn;
  không thay đề TA. Mã US/PAY trùng tên có thể khác nghĩa.
- Chỉ phân tích/thiết kế: lập và sửa Draft, trình duyệt, duyệt/từ chối, điều chỉnh,
  hủy bảng [TA-SPEC §1, §4]. Hợp đồng, bảng giá, sản lượng chỉ đọc qua interface;
  không thiết kế CRUD các module đó.
- Vai trò theo §2: NVKD, KTT, GĐKD. Trạng thái liệt kê trong §3: Draft,
  PendingApproval, Approved, Rejected, Cancelled. Giữ mâu thuẫn để hỏi;
  không thêm trạng thái hoặc chốt luồng cuối cùng khi chưa xác nhận.
- Không tự đưa ký điện tử, phát hành, thuế hay workflow nhiều cấp từ Google Docs
  vào bài TA như yêu cầu bắt buộc.

## Tình huống cần hỏi, chưa phải đáp án nghiệp vụ

| Vị trí TA-SPEC | Vấn đề | Lý do cần xác nhận |
|---|---|---|
| §2 ↔ PAY-01 | Kỳ tháng/quý nhưng duy nhất theo tháng | Ảnh hưởng khóa duy nhất và kỳ được lập |
| §4.3 ↔ PAY-06 | Từ 500 triệu / trên 500 triệu | Chưa thống nhất ai duyệt đúng 500.000.000 đồng |
| §4.4 ↔ PAY-05 | KTT điều chỉnh Approved / cấm mọi sửa đổi | Chưa thể chốt sửa trực tiếp hay bản điều chỉnh |
| §3 ↔ PAY-08 | Sau từ chối ở Rejected / quay Draft | Chưa chốt đích chuyển trạng thái/bước trung gian |
| PAY-04 | Chưa liệt kê dòng dịch vụ bắt buộc | Chưa đủ căn cứ tạo validation chi tiết |

- Bảng trên không đầy đủ; vẫn phải đọc toàn nguồn, dẫn mọi phía và tìm thêm
  thiếu/mơ hồ. Không coi phương án của AI là quyết định đã duyệt.
- PAY-07 cấm tự duyệt. Quyền hủy, phạm vi sửa Draft, làm tròn, VAT, lập lại sau
  hủy, kênh thông báo chưa rõ thì ghi OQ, không tự thêm thành rule.
- Chống trình duyệt trùng theo PAY-04 là hành vi bắt buộc; Idempotency-Key,
  unique constraint hoặc transaction là phương án kỹ thuật cần giải thích.

## Truy vết và kiểm chứng
- Bao phủ US-PAY-01..05, PAY-01..08 và hai NFR §6.
  `NFR-PAY-01` (audit) và `NFR-PAY-02` (lập bảng ≤3 giây với <200 dòng)
  là mã nội bộ; đề không đặt mã NFR. Không đổi thành ≤200 dòng hoặc tự thêm
  percentile/tải đồng thời làm tiêu chuẩn gốc.
- Audit mọi thay đổi trạng thái và mọi điều chỉnh: ai, lúc nào, thay đổi gì
  [TA-SPEC §6]. Giữ OQ về điều chỉnh Approved.
- `docs/design/payment-management/06-traceability-matrix.md` nối yêu cầu + nguồn
  → thành phần → UML → API/lớp/dữ liệu → cách kiểm chứng → trạng thái/OQ.
  Yêu cầu bị chặn vẫn có dòng; không đánh dấu đã đáp ứng.
- Tên trạng thái, class, thao tác, endpoint phải nhất quán giữa mọi tài liệu/sơ đồ.
  PlantUML lưu tại `diagrams/`. Chưa chạy kết xuất thì ghi
  `Chưa kiểm tra kết xuất sơ đồ`.
- Đầu ra theo `.agents/agents/design.md` và `.agents/agents/reviewer.md`;
  giữ bản lần đầu/sau review theo `docs/workflow/README.md`.
