# Sổ nguồn – Bảng thanh toán TA 1–2

Cập nhật: 07/11/2026 (Asia/Ho_Chi_Minh). Đây là chỉ mục và hướng dẫn sử dụng
nguồn, không thay nội dung đặc tả hoặc xác nhận nghiệp vụ thay nhóm.

## Nguồn dùng trong bài

Nguồn nghiệp vụ cho TA 1–2 chỉ gồm TA-PDF và TA-SPEC lưu trong workspace.
Bỏ qua các đường dẫn tới tài liệu nghiệp vụ trực tuyến; không dùng chúng để
bổ sung user story/quy tắc hoặc giải quyết câu hỏi chưa rõ. Tài liệu đồ án
tổng thể chỉ cung cấp bối cảnh, code hiện có chỉ phục vụ khảo sát AS-IS.

| Mã nguồn | Tài liệu/vị trí | Cách dùng |
|---|---|---|
| TA-PDF | [assignment-ta-1-2.pdf](assignment-ta-1-2.pdf), bản sao của BAITAP_TA_1-2.pdf người dùng cung cấp | Đề bài gốc, 3 trang; §1–6 là đặc tả, phần sau §6 là sản phẩm/tiêu chí chấm |
| TA-SPEC | [spec.md](spec.md) | Bản chép nội dung §1–6, giữ nguyên; nguồn làm chuẩn để phân tích/thiết kế TA |
| DATH | [QTKD_DATH.pdf](../QTKD_DATH.pdf) | Bối cảnh đồ án tổng thể; không phải đề TA 1–2 |
| BA-DATH | [BA_QTKD_User_Stories.xlsx](../BA_QTKD_User_Stories.xlsx) | Phân tích có sẵn cho đồ án tổng thể; không coi là đặc tả đã duyệt của TA |
| AS-IS | [src/Qtkd.Api](../../../src/Qtkd.Api) | Code demo hợp đồng, dùng khảo sát hiện trạng; không xác lập nghiệp vụ Bảng thanh toán |

TA-PDF được sao chép nguyên byte từ file đính kèm; SHA-256:
`bc8b34cc847343151a496c2a515a7178bf90a834d5bee909bddcf56179bd218e`.
Nội dung nghiệp vụ TA-SPEC đã được đối chiếu với ba trang PDF trong lần thiết lập;
chỉ khác định dạng Markdown, không sửa các mâu thuẫn.

## Dẫn trang TA-PDF

| Nội dung | Trang |
|---|---|
| §1 phạm vi; §2 thuật ngữ/vai trò; §3 trạng thái | 1 |
| §4.1–4.5, US-PAY-01..05; §5, PAY-01..08 | 2 |
| §6, hai NFR; yêu cầu bài tập và tiêu chí đánh giá | 3 |

Ví dụ: `[TA-SPEC §4.3, US-PAY-03; TA-PDF tr.2]`.
NFR-PAY-01 và NFR-PAY-02 là mã nội bộ, lần lượt ứng với hai gạch đầu dòng §6;
đề không đặt mã NFR.

## Xử lý khác biệt và thông tin chưa rõ

Mâu thuẫn trong đề phải giữ cả hai phía và dẫn trang/mục/US/PAY cụ thể.
Tài liệu đồ án tổng thể và code hiện có không ghi đè TA-SPEC, không được dùng
để tự chọn một cách hiểu hoặc tạo nghiệp vụ mới.

Ghi Open Questions cùng lý do và ảnh hưởng. Khi người phụ trách xác nhận,
ghi riêng quyết định, người/ngày, tham chiếu câu trả lời và tác động;
không sửa hồi tố nguồn gốc.
