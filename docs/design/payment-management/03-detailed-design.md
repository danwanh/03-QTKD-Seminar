# State diagram — Vòng đời Bảng thanh toán

Trạng thái: **Design Pending Approval**. Phạm vi lần này là state diagram cho US-PAY-01..05, không phải bộ LLD/API/dữ liệu hoàn chỉnh. Nguồn được chốt theo `main` và `origin/main` tại commit `821eb4b0a2ce1b1d4d52c4eaf524a57374fbbe14`, sau `git fetch origin` ngày 07/11/2026 (Asia/Saigon).

## 1. Nguồn Markdown và cách chọn phiên bản

| Mã dùng trong tài liệu này | Bản được dùng | Mục liên quan / cách dùng |
|---|---|---|
| TA-SPEC | [Đặc tả gốc](../../requirements/payment-management/spec.md) | §1–6: phạm vi, vai trò, 5 trạng thái, 5 US, PAY-01..08, audit và hiệu năng. Đây là căn cứ nghiệp vụ gốc. |
| SOURCE | [Sổ nguồn](../../requirements/payment-management/sources.md) | Ánh xạ TA-PDF: §1–3 tr.1; §4–5 tr.2; §6 tr.3. Không đọc lại PDF trong lần này. |
| SYS01 | [sys-pay-01-lap-bang-thanh-toan-v01.md](../../analysis/payment-management/sys-pay-01-lap-bang-thanh-toan-v01.md) | Đường dẫn thực trên `main` là **v01**, nhưng tiêu đề và nội dung là **v02 sau xác nhận**. Dùng Phần 1–4 thực có; không suy diễn tồn tại tệp v02 khác. CREATE-01..04, 08..13 và KT-01..05 được tài liệu ghi nhận đã đồng ý; các CREATE còn mở giữ nguyên. |
| SYS02 | [sys-pay-02(v2).md](../../analysis/payment-management/sys-pay-02(v2).md) | B1–B7, A1–A7, hậu điều kiện, OQ-US-PAY-02-01..07 và T1–T4. Bản v1 không thay thế v2. |
| SYS03 | [sys-pay-03-duyet-tu-choi-v2.md](../../analysis/payment-management/sys-pay-03-duyet-tu-choi-v2.md) | Mục 1–2, OQ-P03-01..21; đây là bản đã áp dụng **đề xuất chờ xác nhận**, không phải bản phê duyệt. Đọc cùng [can-xac-nhan.md](../../analysis/payment-management/can-xac-nhan.md) mục 1–2; giữ ID của nguồn. |
| SYS04 | [US-PAY-04 After Review](us-pay-04-after-review/us-pay-04-after-review.md) | Dữ liệu, System Spec, đề xuất kỹ thuật, OQ-02/03: bảng gốc giữ `Approved`, ghi hồ sơ điều chỉnh riêng. |
| SYS04-P04 | [Chatlog After Review, P-04](us-pay-04-after-review/chatlog-minh-chung.md) | Ghi nhận yêu cầu người dùng chọn cách lưu số gốc / hồ sơ riêng / số tiền có hiệu lực. Phạm vi này không xác nhận việc duyệt lại, người duyệt hoặc thời điểm áp dụng. |
| SYS04-OQ | [Các câu hỏi Before Review](us-pay-04-before-review/us-pay-04-issues.md) | OQ-01..03 và hai hướng A/B; chỉ đối chiếu nền của bản After Review. Không chọn B thay A. |
| SYS05 | [Đặc tả hủy bảng nháp](../../requirements/payment-management/spec-usecase-us-pay-05.md) | Bảng UC: Draft → Cancelled; quyền, lý do và kiểm soát ghi vẫn là giả định/đề xuất trong nguồn. |
| SYS05-OQ | [Phân tích US-PAY-05](../../requirements/payment-management/us-pay-05-analysis.md) | Mục 2–4: OQ-PAY05-01..06. Không lấy trạng thái `Terminated` trong ví dụ Mermaid làm trạng thái bảng. |
| REVIEW01 | `docs/review/payment-management/ai-review-01.md` **trong commit main**, đọc bằng `git show main:…` | Mục 3–4: lệch tên v01/v02, điều kiện trùng khi sửa và R01-OQ-01 về đối soát dữ liệu sửa tay. Chỉ dùng để nhận diện giới hạn đã có; không coi nhận xét AI là phê duyệt hoặc sửa báo cáo. |

Đã đối chiếu thêm các sequence lập/lưu/sửa Draft, trình duyệt v2, activity duyệt và sequence điều chỉnh After Review, sequence hủy trong repo. Tài liệu cũ, snapshot và chatlog chỉ dùng truy nguồn; không ghép mọi phiên bản thành các quy tắc cùng có hiệu lực. Không dùng PDF/Excel đồ án tổng thể, tài liệu nghiệp vụ trực tuyến hoặc các review cục bộ chưa commit để đặt business rule. Không khảo sát AS-IS hay sửa mã ứng dụng trong lần vẽ vòng đời này. [TA-SPEC §1; SOURCE; SYS01..05]

## 2. Danh mục tên dùng chung

Tên thao tác dưới đây là tên sự kiện ở mức mô hình; không chốt class, endpoint, schema hoặc công nghệ mới. Tên gọi khác trong sequence có sẵn được ánh xạ ở cột cuối, không sửa các sequence ngoài phạm vi. [ĐỀ XUẤT KỸ THUẬT — biểu diễn UML cho TA-SPEC §3–4]

| Tên | Ý nghĩa | Đối chiếu nguồn / tên đã có |
|---|---|---|
| `Draft`, `PendingApproval`, `Approved`, `Rejected`, `Cancelled` | Đúng 5 trạng thái của bảng gốc. | [ĐẶC TẢ] TA-SPEC §3; không phải enum trạng thái hợp đồng. |
| `saveDraft(create)` / `saveDraft(update)` | Lưu mới / cập nhật bản nháp. | SYS01 Phần 3 bước 8–11, A1; `saveDraft(actor, mode, …)` trong sequence lưu/sửa Draft. |
| `submit` | Trình duyệt. | SYS02 B1–B5; `submit` trong sequence v2; `SubmitForApprovalAsync` trong sequence tổng quan. |
| `approve` / `reject` | Duyệt / từ chối. | TA-SPEC §4.3; SYS03 bước 3–8 / A3; `ApproveAsync` / `RejectAsync` trong sequence tổng quan. |
| `reopen` | Người tạo mở lại Rejected thành Draft. | Chỉ là [GIẢ ĐỊNH – Cần xác nhận] theo SYS03 OQ-P03-02/12; chưa có hợp đồng API cho thao tác này. |
| `cancel` | Hủy bảng. | TA-SPEC §4.5; SYS05; `CancelPaymentSheetAsync` trong sequence hủy. Hủy Rejected là nhánh riêng chờ OQ-P03-12. |
| `adjust` | Ghi nhận điều chỉnh. | TA-SPEC §4.4; SYS04; `Adjust` trong sequence After Review. Không đồng nhất việc ghi hồ sơ với việc có hiệu lực. |
| `G-*`, `T*` | Guard và mã truy vết của sơ đồ. | Mã nội bộ mới trong tài liệu này, không phải mã TA hoặc AC đã được phê duyệt. |

## 3. Guard của các thao tác

Các guard diễn đạt điều kiện nghiệp vụ/kiểm tra ở mức thiết kế; **phần mang OQ chưa đủ điều kiện coi là chính sách hoàn chỉnh**. Việc nguồn đã viết một đề xuất vào luồng chính không làm OQ tự đóng.

| Guard | Điều kiện và nguồn | Phần còn mở |
|---|---|---|
| G-CREATE | NVKD; hợp đồng Active/chưa hết hiệu lực; đúng kỳ tháng/quý cấu hình hợp đồng; có bảng giá hiệu lực; sản lượng sử dụng đã đối soát; không có **bảng khác** chưa Cancelled trùng hợp đồng/kỳ; đủ trường bắt buộc. Tính lại tiền theo sản lượng × đơn giá tại thời điểm tính. [ĐẶC TẢ: TA-SPEC §4.1, PAY-01..03; QUYẾT ĐỊNH được SYS01 Phần 1–2 ghi nhận: CREATE-01..04/11/12; KT-01..04] | SYS01 CREATE-05/06/07/11a/16/17. Chưa có danh sách trường, cách gom dòng/làm tròn hoặc chính sách kỳ chồng lấn cuối cùng. |
| G-SAVE | Bảng còn Draft; NVKD là người lập; hợp đồng còn hiệu lực; dữ liệu sửa thuộc phạm vi kỳ, sản lượng, bảng giá hợp lệ, dịch vụ, ghi chú; kiểm tra lại điều kiện nguồn/kỳ/trùng khi lưu, **loại chính bảng đang sửa** khỏi tập trùng. Nguồn đổi cần đối chiếu và xác nhận trước khi áp dụng. [SYS01 Phần 1 CREATE-03/08/09/10/11/12, Phần 2 KT-01/02/04, Phần 3 A1/A9/E9; sequence sửa/lưu] | Các mục mở của G-CREATE; R01-OQ-01 trong REVIEW01 mục 4 về đối soát dữ liệu sửa tay. Không coi trạng thái đã đối soát của nguồn tự xác nhận mọi giá trị NVKD sửa. |
| G-SUBMIT | Bảng còn Draft; NVKD; tổng không âm; đủ dòng dịch vụ bắt buộc; yêu cầu chưa được xử lý và phiên bản hiện hành khi ghi. [ĐẶC TẢ: TA-SPEC §4.2, PAY-04; ĐỀ XUẤT KỸ THUẬT: SYS02 B1–B5, T1/T2] | OQ-US-PAY-02-01/02/04/05/06/07: danh mục, điểm biên, người được trình, phân công, dữ liệu đã trình, tổng tiền. G1 chỉ người lập được trình là phương án đang mở. |
| G-APPROVE | Bảng còn PendingApproval; người duyệt đúng thẩm quyền; không phải người lập. Dưới 500 triệu là KTT, trên 500 triệu là GĐKD. [ĐẶC TẢ: TA-SPEC §3, §4.3, PAY-06/07; SYS03 P1–P4] | OQ-P03-01: đúng 500 triệu; 03/04: cơ sở tiền và định nghĩa người lập; 07/14/19: duyệt thay/giao cụ thể; 21: người điều chỉnh duyệt lại. Không áp dụng đề xuất GĐKD duyệt thay bảng dưới ngưỡng như quyền chính thức. |
| G-REJECT | Điều kiện người ra quyết định như G-APPROVE; có lý do từ chối. [ĐẶC TẢ: TA-SPEC §4.3, PAY-08; SYS03 A3] | OQ-P03-02: trạng thái đích; 09/16: danh mục, giới hạn 10–500 ký tự và quyền sửa lý do chỉ là đề xuất. Không biến các số này thành validation gốc của TA. |
| G-REOPEN | Bảng Rejected; NVKD là người tạo. [GIẢ ĐỊNH – Cần xác nhận: SYS03 OQ-P03-02/12] | Blocked by OQ-P03-02/12; TA chưa quy định sự kiện mở lại hoặc chủ thể. |
| G-CANCEL | Bảng Draft và người thực hiện có quyền hủy; có lý do nếu chính sách được xác nhận yêu cầu. [ĐẶC TẢ: TA-SPEC §3, §4.5; GIẢ ĐỊNH – Cần xác nhận: SYS05, SYS05-OQ mục 2] | OQ-PAY05-02/03: ai có quyền và lý do có bắt buộc hay không. Không áp quyền Admin/Trưởng phòng được gợi ý trong SYS05-OQ vì TA-SPEC §2 chỉ có NVKD, KTT, GĐKD. |
| G-CANCEL-REJECTED | Bảng Rejected; quyền và lý do phải được xác nhận riêng cho nhánh này. [GIẢ ĐỊNH – Cần xác nhận: SYS03 OQ-P03-12] | SYS03 đề xuất hủy trực tiếp nhưng SYS05 tiền điều kiện 3 và nhánh 6c chỉ nhận Draft. Blocked by OQ-P03-12 và OQ-PAY05-01/02/03. Không suy diễn quyền mở lại đồng nghĩa quyền hủy. |
| G-ADJUST | Bảng gốc Approved; KTT; có biên bản xác nhận đính kèm; nội dung/biên bản đạt tiêu chí và cơ sở tính còn khớp. [ĐẶC TẢ: TA-SPEC §4.4; lựa chọn A được ghi nhận tại SYS04-P04; ĐỀ XUẤT KỸ THUẬT: SYS04 System Spec và đề xuất kỹ thuật] | SYS04 OQ-02: tiêu chí/phạm vi; OQ-03: duyệt lại, hiệu lực, thứ tự nhiều hồ sơ và dữ liệu đã chuyển kế toán. Ghi nhận hồ sơ không tự đổi số tiền đang có hiệu lực. |
| G-READJUST | Điều chỉnh theo đề xuất duyệt lại trong SYS03: có biên bản, phân công lại và kiểm tra người điều chỉnh không tự duyệt lại. [GIẢ ĐỊNH – Cần xác nhận: SYS03 OQ-P03-10/17/21] | Blocked by OQ-P03-17/21 và SYS04 OQ-03. Đây là lựa chọn chưa thống nhất với SYS04 After Review, không được ghép vào G-ADJUST như một bước chắc chắn. |

Lệnh cấm thao tác sau khi hợp đồng hết hiệu lực và cập nhật nguồn chỉ được SYS01 xác nhận trong phạm vi tạo/sửa Draft; ảnh hưởng sang trình, duyệt, điều chỉnh và hủy còn **CREATE-18**. Không tự thêm lệnh cấm hoặc cập nhật nguồn vào các guard UC khác. [SYS01 Phần 4 CREATE-18]

## 4. Truy vết chuyển trạng thái và phản ứng nội bộ

| Mã | Nguồn → đích / phản ứng | Sự kiện, guard, action | Căn cứ và trạng thái |
|---|---|---|---|
| T01 | Khởi tạo → Draft | Khi lưu mới thỏa G-CREATE: lưu bảng/dòng, ghi audit. | [ĐẶC TẢ] TA-SPEC §4.1, PAY-01..03, §6; SYS01 bước 8–11. Trong UML, cạnh từ nút khởi đầu chỉ có effect; không gán trigger/guard cho cạnh initial. Điều kiện được kiểm tra trước khi khởi tạo. |
| T02 | Nội bộ Draft | `saveDraft(update) [G-SAVE] / tính lại; lưu; ghi audit`. | [ĐẶC TẢ] US-PAY-01; SYS01 A1/A9/E9. Giữ Draft, không tạo lượt vào/ra trạng thái mới. |
| T03 | Draft → PendingApproval | `submit [G-SUBMIT] / ghi audit; ghi nhận yêu cầu thông báo`. | [ĐẶC TẢ] §4.2, PAY-04, §6; [ĐỀ XUẤT KỸ THUẬT] SYS02 B5–B7, T2/T3. Luồng gốc có căn cứ; guard chi tiết vẫn có OQ. |
| T04 | PendingApproval → Approved | `approve [G-APPROVE] / lưu quyết định; ghi audit`. | [ĐẶC TẢ] §3, §4.3, PAY-06/07, §6; SYS03 bước 4–8. Điểm biên và quyền bổ sung chưa chốt. |
| T05 | PendingApproval → Rejected | `reject [G-REJECT] / lưu lý do; ghi audit`. | [ĐẶC TẢ — một phía mâu thuẫn] §3; SYS03 A3. Nét đứt vì xung đột PAY-08. |
| T06 | PendingApproval → Draft | `reject [G-REJECT] / lưu lý do; ghi audit`. | [ĐẶC TẢ — phía còn lại] PAY-08. Nét đứt; Blocked by OQ-P03-02 (= OQ-PAY05-01 về trạng thái sau từ chối). |
| T07 | Rejected → Draft | `reopen [G-REOPEN] / ghi audit`. | [GIẢ ĐỊNH – Cần xác nhận] SYS03 OQ-P03-02/12. Không tự biến Rejected thành trạng thái cuối, cũng không mặc định tự chuyển Draft. |
| T08 | Rejected → Cancelled | `cancel [G-CANCEL-REJECTED] / ghi audit`. | [GIẢ ĐỊNH – Cần xác nhận] SYS03 OQ-P03-12 ↔ SYS05 tiền điều kiện 3, nhánh 6c. Nét đứt để người phụ trách thống nhất. |
| T09A | Nội bộ Approved | `adjust [G-ADJUST] / lưu hồ sơ riêng; ghi audit`. | SYS04 System Spec bước 1–4, SYS04-P04: bảng gốc giữ số liệu và trạng thái Approved. Đây là lựa chọn của bản After Review; điều kiện chi tiết và hiệu lực hồ sơ vẫn mở. Không vẽ trạng thái của hồ sơ thành trạng thái bảng. |
| T09B | Approved → PendingApproval | `adjust [G-READJUST] / ghi audit; yêu cầu duyệt lại`. | [GIẢ ĐỊNH – Cần xác nhận] SYS03 OQ-P03-17/21. Nét đứt, không phải bước tiếp theo bắt buộc của T09A. Cần thống nhất với SYS04 OQ-03. |
| T10 | Draft → Cancelled | `cancel [G-CANCEL] / ghi audit`. | [ĐẶC TẢ] §3, §4.5, §6; SYS05. Chưa tự chốt quyền và lý do. |
| T11 | Cancelled → nút kết thúc | Kết thúc vòng đời bảng đã hủy. | [ĐẶC TẢ] §4.5 không dùng lại; SYS01 CREATE-02/KT-03 giữ bản cũ, cho tạo **bảng mới**. Nút kết thúc không biểu diễn xóa dữ liệu, không cần audit đổi trạng thái thêm. |

Nét đứt thể hiện các cách xử lý để đối chiếu, **không phải nhiều chuyển đồng thời cùng chạy**. Sau xác nhận phải chọn và đồng bộ với UC/sequence; không thêm guard lựa chọn A/B vào hệ thống như một cấu hình nghiệp vụ mới. Approved không nối nút kết thúc vì còn thao tác ghi hồ sơ điều chỉnh; Rejected không nối nút kết thúc vì đường xử lý còn mở. [TA-SPEC §3, §4.4, PAY-05/08; SYS03 OQ-P03-02/10/12/17/21; SYS04]

## 5. OQ còn ảnh hưởng vòng đời

Bảng này dẫn lại ID từ nguồn, không đổi trạng thái OQ của BA hoặc tự ghi nhóm đã phê duyệt.

| Vấn đề | Mọi phía cần đối chiếu | ID / trạng thái |
|---|---|---|
| Ngưỡng đúng 500 triệu | TA-SPEC §4.3 từ 500 triệu ↔ PAY-06 trên 500 triệu; SYS02 B4 vẫn chặn mô tả điểm biên; SYS03 đề xuất GĐKD ở điểm biên. | OQ-US-PAY-02-02 = OQ-P03-01; Cần xác nhận. |
| Trạng thái sau từ chối | TA-SPEC §3 ↔ PAY-08; SYS03 đề xuất Rejected rồi người tạo mở lại; SYS05-OQ mục 2 giữ hai kịch bản. | OQ-P03-02, OQ-PAY05-01; Cần xác nhận. |
| Hủy Rejected trực tiếp | SYS03 hậu điều kiện/OQ-P03-12 cho hủy trực tiếp ↔ SYS05 tiền điều kiện 3 và nhánh 6c chỉ cho Draft; TA §4.5 chỉ nêu Draft. | OQ-P03-12, OQ-PAY05-01/02/03; Cần xác nhận. |
| Điều chỉnh có đổi trạng thái bảng gốc không | TA §4.4 ↔ PAY-05; SYS03 OQ-P03-10/17/21 đề xuất Approved → PendingApproval và dùng số hiệu biên bản ↔ SYS04 After Review giữ Approved, hồ sơ riêng, yêu cầu biên bản đính kèm, để mở duyệt lại/hiệu lực. | Giữ lựa chọn A của SYS04-P04 trong phạm vi đã ghi nhận. Quy trình duyệt lại và khác biệt số hiệu/file: OQ-P03-17/21, SYS04 OQ-02/03; Cần xác nhận. |
| Lập lại sau hủy | SYS05-OQ OQ-PAY05-04 còn ghi giả định ↔ SYS01 CREATE-02, KT-03 đã có bản ghi lời xác nhận cho tạo bảng mới. | Sử dụng quyết định SYS01 cho thao tác tạo mới, không hồi tố sửa OQ của SYS05; không vẽ Cancelled → Draft. |
| Quyền/chính sách chưa đủ | TA §4.1–4.5; SYS01 Phần 4; SYS02 OQ-01/03..07; SYS03 OQ-03..21; SYS04 OQ-02/03; SYS05-OQ OQ-02/03/05/06; REVIEW01 R01-OQ-01. | Giữ ID nguồn; phần phụ thuộc tiếp tục Cần xác nhận. Không thêm thời hạn/nhắc duyệt, Admin, công thức VAT, SLA hủy ≤500 ms hoặc trạng thái Terminated thành rule gốc. |

## 6. Thông báo, audit, chống lặp và lỗi

- **[ĐẶC TẢ] Audit** mọi chuyển trạng thái thành công và mọi điều chỉnh: ai, lúc nào, thay đổi gì; áp dụng cả các cạnh nét đứt nếu sau này được chọn. Không cần tạo audit đổi trạng thái cho retry không làm đổi trạng thái. [TA-SPEC §6, NFR-PAY-01; SYS02 A2/hậu điều kiện]
- **[ĐỀ XUẤT KỸ THUẬT] Ghi nguyên tử** dữ liệu và audit, kiểm tra trạng thái/phiên bản tại điểm ghi: guard không đạt hoặc giao dịch ghi thất bại thì yêu cầu đó không tạo chuyển trạng thái. Nếu phiên khác đã chuyển trạng thái, tải lại bản hiện hành; không ép dữ liệu quay về trạng thái cũ. Mục đích là tránh lưu dở dang/mất audit; ghi từng phần là phương án đơn giản hơn nhưng không đáp ứng tính nhất quán được các UC mô tả. [SYS01 KT-04/E10; SYS02 T1/T2, A3/A6; SYS03 A4/A7; SYS04 System Spec dòng thay thế; SYS05 nhánh 7a/7b]
- **[ĐẶC TẢ] Trình trùng** không tạo lần chuyển/audit trạng thái thứ hai. **[ĐỀ XUẤT KỸ THUẬT]** nhận diện yêu cầu lặp và kiểm tra phiên bản; yêu cầu lặp trả kết quả đã ghi. Trạng thái xử lý thông báo nằm ngoài máy trạng thái bảng. Nếu đã trình thành công rồi gửi lỗi, giữ PendingApproval và gửi lại thông báo, không trình lại. [PAY-04; SYS02 B2/B5, A2/A7, T1/T3]
- Thời hạn 3 ngày làm việc và lịch nhắc trong SYS03 OQ-P03-11/18 chưa được xác nhận; không thêm event tự duyệt, tự từ chối hoặc trạng thái quá hạn. Kênh nhận thông báo còn SYS02 OQ-03, SYS03 OQ-P03-08/20; không mặc định email là bắt buộc. [TA-SPEC §3–4; SYS02/SYS03]
- **[ĐẶC TẢ] Hiệu năng** NFR-PAY-02: chức năng lập bảng phản hồi ≤3 giây với **<200 dòng**, không đổi thành ≤200 hoặc gán cho mọi event; cách đo bổ sung được SYS01 CREATE-13/KT-05 ghi nhận. Đây là tiêu chí kiểm thử, không phải guard phụ thuộc đồng hồ hoặc bằng chứng đã đạt. [TA-SPEC §6; SYS01 Phần 1–3]

## 7. Danh mục sơ đồ và kiểm chứng

| Tệp | Mục đích / phạm vi | Yêu cầu | Kết xuất |
|---|---|---|---|
| [state-machine.puml](diagrams/state-machine.puml) | Vòng đời một bảng gốc; chuyển trạng thái và phản ứng nội bộ; các lựa chọn còn mở. | US-PAY-01..05, PAY-01..08; audit NFR-PAY-01; giới hạn NFR-PAY-02. | Chưa kiểm tra kết xuất sơ đồ. |

Ảnh: [SVG](diagrams/state-machine.svg), [PNG](diagrams/state-machine.png). Kết quả kiểm tra sẽ được cập nhật sau khi chạy công cụ. Bản mới này không thay các sequence hoặc snapshot đã có; không ghi vào `docs/workflow/prompt-log.md` theo yêu cầu trực tiếp của người dùng.
