---
name: sys-spec
description: Viết đặc tả use case hệ thống SYS-PAY-0N (actor, tiền/hậu điều kiện, dòng cơ bản/thay thế, NFR, AC dẫn xuất, Open Questions) cho một US-PAY của module Bảng thanh toán, bám TA-SPEC và dẫn nguồn từng dòng.
---

# Skill: sys-spec – Đặc tả use case hệ thống

Vai trò: **ba** trong [AGENTS.md](../../AGENTS.md). Đọc AGENTS.md và
[ngữ cảnh dùng chung](../_shared/payment-context.md) trước khi làm.

## Đầu vào

- Tham số: số US (01..05), vd. "dùng skill sys-spec cho US-PAY-02".
- Đọc toàn bộ [TA-SPEC](../../docs/requirements/payment-management/spec.md),
  không chỉ mục của US được giao (quy tắc PAY và §3/§6 tác động chéo).
- Đọc nếu có: `docs/analysis/payment-management/open-questions.md`,
  `requirements-analysis.md` và các `sys-pay-*.md` khác để tái sử dụng OQ/AC.
- Mẫu định dạng: [sys-pay-03-duyet-tu-choi.md](../../docs/analysis/payment-management/sys-pay-03-duyet-tu-choi.md).

## Đầu ra

`docs/analysis/payment-management/sys-pay-0N-<slug>.md`, slug gợi ý:
01 `lap-bang`, 02 `trinh-duyet`, 03 `duyet-tu-choi`, 04 `dieu-chinh`,
05 `huy-bang-nhap`. File đã tồn tại thì chỉ bổ sung phần thiếu/sai có căn cứ,
không viết lại toàn bộ; nêu thay đổi trong câu trả lời.

## Các bước

1. **Liệt kê căn cứ**: câu nguyên văn của US, mọi PAY liên quan, §2/§3/§6.
   Bảng gợi ý (phải kiểm tra lại trên đặc tả):

   | US | PAY/§ thường liên quan |
   |---|---|
   | 01 Lập/sửa Draft | PAY-01, 02, 03; §2 kỳ thanh toán; NFR-PAY-02 |
   | 02 Trình duyệt | PAY-04, 06 (chọn người nhận thông báo), §3 |
   | 03 Duyệt/từ chối | PAY-05, 06, 07, 08; §3; NFR-PAY-01 |
   | 04 Điều chỉnh Approved | PAY-05 (mâu thuẫn), §4.4 biên bản; NFR-PAY-01 |
   | 05 Hủy Draft | §3, §4.5; quyền hủy chưa rõ |

2. **Phần 1 – bảng use case** đúng các hàng của mẫu: Tên (SYS-PAY-0N), Tác nhân
   (chính/liên quan), Mục tiêu, Kích hoạt, Tiền điều kiện (P1..), Hậu điều kiện
   (thành công/thất bại), Dòng cơ bản (đánh số), Dòng thay thế, Yêu cầu phi chức năng.
   - Mỗi bước/điều kiện kết thúc bằng nhãn + dẫn nguồn.
   - Dòng thay thế đặt tên theo bước rẽ nhánh (A4 rẽ từ bước 4); nhánh con A4.2.
   - Bắt buộc có nhánh: sai trạng thái, sai quyền, dữ liệu không hợp lệ, thao tác
     đồng thời/trùng (nếu đề có yêu cầu), lỗi lưu kể cả lỗi audit.
   - Bước UI/điều hướng không có trong đề → `[ĐỀ XUẤT KỸ THUẬT]`.
   - NFR: nêu NFR-PAY-01/02 áp dụng hay **không áp dụng** và vì sao; không tự
     thêm SLA cho chức năng khác ngoài lập bảng.
3. **Phần 2 – Điểm cần xác nhận**: bảng OQ theo mẫu AGENTS.md (ID, Loại, Vị trí mọi
   nguồn kèm trích dẫn ngắn, Vấn đề, Lý do, Lựa chọn, Ảnh hưởng tới Phần 1,
   Trạng thái `Cần xác nhận`). Tái sử dụng ID đã có; mới thì `OQ-P0N-kk`.
   Mỗi `Blocked by OQ-…` ở Phần 1 phải có dòng tương ứng ở Phần 2 và ngược lại.
4. **Phần 3 – Acceptance criteria**: bảng `ID | Given/When/Then | Nhãn | Nguồn | OQ`.
   - `[ĐẶC TẢ]` khi gần nguyên văn; còn lại `[AC dẫn xuất]` nối về câu gốc.
   - AC phụ thuộc OQ vẫn ghi, cột OQ điền `Blocked by OQ-…`, không chọn phía.
   - Mã `AC-US0N-kk` là mã tự đặt; ghi chú điều đó ở đầu bảng.
5. **Đầu file**: khối trích dẫn Nguồn, Trạng thái "Bản AI soạn lần đầu, chưa được
   nhóm/người phụ trách xác nhận", giải nghĩa nhãn – như mẫu.

## Không được

- Thêm vai trò, trạng thái, ngưỡng, thuế, SLA, kênh thông báo, công thức không có nguồn.
- Chọn KTT/GĐKD cho đúng 500 triệu, chọn Rejected/Draft, chọn cách điều chỉnh Approved,
  chốt kỳ tháng/quý, liệt kê "dòng dịch vụ bắt buộc".
- Chốt endpoint/schema/class (việc của design); chỉ được gợi ý có nhãn.
- Dùng Excel/DATH làm đáp án.

## Tự kiểm trước khi trả lời

- [ ] Mọi hàng Phần 1 có nhãn + nguồn; không còn câu khẳng định không dẫn nguồn.
- [ ] Mọi PAY liên quan ở bước 1 xuất hiện ít nhất một lần.
- [ ] Mọi `Blocked by OQ-…` ↔ dòng OQ khớp hai chiều (`grep -o "OQ-P0N-[0-9]*"`).
- [ ] Mỗi dòng cơ bản/thay thế có ít nhất một AC; mỗi AC có nguồn.
- [ ] Tên trạng thái đúng 5 giá trị §3.
- Ghi lần chạy vào [prompt-log](../../docs/workflow/prompt-log.md) theo
  [quy trình](../../docs/workflow/README.md).
