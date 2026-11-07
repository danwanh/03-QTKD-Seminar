# Sổ nguồn – Bảng thanh toán TA 1–2

Cập nhật: 07/11/2026 (Asia/Ho_Chi_Minh). Đây là chỉ mục và hướng dẫn sử dụng
nguồn, không thay nội dung đặc tả hoặc xác nhận nghiệp vụ thay nhóm.

## Nguồn dùng trong bài

| Mã nguồn | Tài liệu/vị trí | Cách dùng |
|---|---|---|
| TA-PDF | [assignment-ta-1-2.pdf](assignment-ta-1-2.pdf), bản sao của BAITAP_TA_1-2.pdf người dùng cung cấp | Đề bài gốc, 3 trang; §1–6 là đặc tả, phần sau §6 là sản phẩm/tiêu chí chấm |
| TA-SPEC | [spec.md](spec.md) | Bản chép nội dung §1–6, giữ nguyên; nguồn làm chuẩn để phân tích/thiết kế TA |
| GREF | [spec nghiệp vụ + hệ thống](https://docs.google.com/document/d/1I_IshVHK8r2lkjtv5ekD5JQV4SRdI44MbvJ8ouGZlis/edit?tab=t.wacxj1o2c65v) | Tham khảo nghiệp vụ/user story và phân công; không thay đề TA |
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

## Các tab Google Docs liên quan đã đọc

Đã truy cập qua Google Drive ngày 07/11/2026. Đây là bản trực tuyến có thể thay đổi;
muốn tái lập một phân tích cần ghi ngày đọc, tab, tiêu đề, US/AC và trích dẫn ngắn.
Không coi ngày đọc là ngày nhóm xác nhận nghiệp vụ.

| Tab ID | Tiêu đề | Nội dung đã dùng để thiết lập |
|---|---|---|
| `t.wacxj1o2c65v` | link figma | Bảng phân công; hàng “Agent, rules và tích hợp workspace” khớp nhiệm vụ hiện tại |
| `t.odszmg6tlwy3` | Quản lý bảng thanh toán | Use case của đồ án tổng thể, có lập/đối soát, nhiều bước duyệt, ký, phát hành, điều chỉnh |
| `t.edjyesp1asb5` | User story btt | US-PAY-01..17 của tài liệu tham khảo, không phải 5 US của TA |
| `t.hwohsapr5cqu` | Cần xác nhận | Bảng câu hỏi/giả định; cột kết luận không phải bằng chứng đã được xác nhận |
| `t.b0hae4rvvzt` | Business rule | PAY-01..07 của đồ án, có khác nghĩa so với mã TA |
| `t.xxuu2cz463qo` | State | API không trả văn bản; không tuyên bố đã đọc sơ đồ/ảnh trong tab |

## Những chỗ dễ trộn nguồn

| Chủ đề | TA 1–2 | Google Docs tham khảo | Cách xử lý trong cấu hình |
|---|---|---|---|
| Người lập | NVKD, §2/§4.1 | Phòng Kế toán, UC-PAY-01/US-PAY-01 | Giữ NVKD trong TA; ghi khác biệt khi đối chiếu |
| PAY-06 | Ngưỡng tiền và GĐKD/KTT, §5 | Điều kiện gửi ký điện tử, tab Business rule | Dùng tiền tố TA:PAY-06 / GREF:PAY-06 |
| Trạng thái/phạm vi | 5 trạng thái §3, phạm vi §1 | Có Calculated, Reconciled, Submitted, Signing, Signed, Issued… | Không tự mở rộng phạm vi TA |
| US-PAY-04 | Điều chỉnh Approved, §4.4 | Một chức năng khác trong bộ 17 US | Dẫn kèm mã nguồn và tab; không nối theo mã giống nhau |
| Điều chỉnh/từ chối | Đề TA chứa mâu thuẫn giữa các mục | Tham khảo đưa ra quy trình và giả định riêng | Vẫn ghi OQ của TA, chờ xác nhận áp dụng |

Mâu thuẫn trong cùng đề phải giữ cả hai phía. Nội dung tham khảo hoặc code hiện có
không có quyền tự ghi đè TA-SPEC. Khi người phụ trách xác nhận thay đổi, ghi riêng
quyết định, người/ngày/xác nhận và tác động; không sửa hồi tố nguồn gốc.
