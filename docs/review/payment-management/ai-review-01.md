# AI review 01 — SYS-PAY-01 và sequence lập bảng thanh toán

Ngày review: 07/11/2026 (Asia/Saigon). Vai trò: reviewer trong chat hiện tại, không chạy subagent. Phạm vi theo yêu cầu: tìm điểm dư, thiếu, conflict trong hai file được chỉ định; đọc thêm interaction được tham chiếu để kiểm tra đúng phần lưu. Không sửa tài liệu đầu vào hoặc tự xác nhận nghiệp vụ.

## 1. Kết luận và phạm vi kiểm chứng

**Cần chỉnh sửa** đối với cặp tài liệu được review: có lệch phiên bản/đường dẫn, tiền điều kiện chưa thống nhất với luồng sửa và một số chi tiết tương tác chưa đủ rõ để bàn giao triển khai. Có **1 nhận xét mức Cao, 4 mức TB và 1 đề xuất mức Thấp** ở mục 3. Các nhận xét TB về sơ đồ là thiếu mô tả cần làm rõ, không phải bằng chứng ứng dụng đã chạy sai.

**Chờ xác nhận nghiệp vụ** đối với các CREATE còn mở và câu hỏi mới R01-OQ-01 tại mục 4. Reviewer không chọn đáp án thay người phụ trách. Các chi tiết được tài liệu ghi nhận là đã xác nhận vẫn được đối chiếu theo nhãn đó; không mặc định xem chúng là yêu cầu nguyên văn của TA.

**Chưa đủ đầu vào review toàn bộ thiết kế module**: các file HLD/LLD, API, dữ liệu, ma trận và UML khác trong danh mục `docs/design/payment-management/README.md:10–23` chưa tồn tại. Đây là giới hạn ngoài phạm vi hai file được giao, không phải yêu cầu bổ sung toàn bộ thiết kế vào sơ đồ SYS-PAY-01.

Tiêu chí hoàn thành lần review: đọc đặc tả gốc cục bộ và hai file được giao; đọc interaction lưu/sửa và chỉ mục liên quan; dẫn vị trí, căn cứ, tác động và cách xác minh cho từng nhận xét; kiểm tra cú pháp/render; ghi báo cáo mới, giữ nguyên đầu vào.

## 2. Nguồn và bản đã đọc

| Mã | Tài liệu | Cách dùng / giới hạn |
|---|---|---|
| TA-SPEC | [spec.md](../../requirements/payment-management/spec.md), toàn bộ §1–6 | Nguồn nghiệp vụ gốc được đọc độc lập trước khi đối chiếu nội dung review. |
| SOURCE | [sources.md](../../requirements/payment-management/sources.md) | Quy định phạm vi nguồn và ánh xạ trang PDF: §1–3 tr.1; §4–5 tr.2; §6 tr.3. |
| BA01 | [sys-pay-01-lap-bang-thanh-toan-v01.md](../../analysis/payment-management/sys-pay-01-lap-bang-thanh-toan-v01.md), dòng 1–84 | File thực tế mang tiêu đề v02 và chứa quyết định sau xác nhận; review nội dung thực tế này, không suy diễn có một bản v01 thuần đề khác. |
| SEQ01 | [sequence-sys-pay-01-lap-bang-thanh-toan.puml](../../design/payment-management/diagrams/sequence-sys-pay-01-lap-bang-thanh-toan.puml), dòng 1–132 | Sơ đồ chính được giao. |
| SAVE01 | [sequence-sys-pay-01-luu-draft.puml](../../design/payment-management/diagrams/sequence-sys-pay-01-luu-draft.puml), dòng 1–159 | Interaction được SEQ01 tham chiếu, cần đọc để kiểm tra lưu/audit/chống lặp. |
| EDIT01 | [sequence-sys-pay-01-sua-draft.puml](../../design/payment-management/diagrams/sequence-sys-pay-01-sua-draft.puml), toàn bộ | Đối chiếu nhánh A1 của cùng Use Case và hợp đồng lưu dùng chung. |
| IDX | [README sơ đồ](../../design/payment-management/diagrams/README.md), toàn bộ; [README thiết kế](../../design/payment-management/README.md), toàn bộ | Giới hạn TO-BE, lựa chọn kỹ thuật, quy tắc lỗi E10 và danh mục tài liệu. Không kiểm lại các tuyên bố AS-IS bằng mã nguồn trong lần review này. |
| LOG | [prompt-log.md](../../workflow/prompt-log.md), toàn bộ | Đối chiếu lịch sử được ghi về v01/v02 và kiểm chứng sơ đồ. |
| RULE | [AGENTS.md](../../../AGENTS.md), toàn bộ; [quy trình minh chứng](../../workflow/README.md), toàn bộ | Quy tắc reviewer, nguồn, OQ, phiên bản và phạm vi ghi file. |

TA-PDF **chưa được trích xuất/đọc trực tiếp trong lần review này**: môi trường kiểm tra không có `pdftotext` trong PATH; Python được tìm thấy không có `pypdf`, `pdfplumber`, `fitz`. Mọi dẫn trang TA-PDF dưới đây là ánh xạ theo SOURCE, không phải tuyên bố đã kiểm chứng lại PDF. Không dùng tài liệu nghiệp vụ trực tuyến, Excel hoặc PDF đồ án tổng thể làm căn cứ.

BA01:17–20, 26–49 ghi các trích dẫn USER-01 và lời đồng ý USER-02. Reviewer đọc được bản ghi này và LOG, nhưng không có toàn văn cuộc trao đổi gốc USER-01/02/03 trong ngữ cảnh hiện tại để xác minh độc lập phạm vi phê duyệt. Không kết luận các xác nhận đó sai hoặc không tồn tại. Lỗi phiên bản ở R01-01 làm việc truy lại bản trước/sau khó hơn.

Mốc Git tham chiếu: `6b60debbe63d2bc2e61c9720089c0a5b37a80e5d`. Cả bốn file BA01/SEQ01/SAVE01/EDIT01 đang untracked khi bắt đầu; commit này không đại diện cho nội dung đang review. SHA-256 của bản thực tế:

| Mã | SHA-256 |
|---|---|
| BA01 | `E6055B080BCED4013069E36320073FF3F3DC691AB47DAAED5674BCCFCD5BC508` |
| SEQ01 | `C1CCB2B5942410C24A0F7746E7F0E0E758E413D56EE6B420A7CC0A55F9A45DC8` |
| SAVE01 | `9723BFAF405A21ED502B517995E56D7AF147EE4E470B28EB0EB150B8C6743C76` |
| EDIT01 | `8C0EBACC7E2BD7DC0D8278EB61908BC9B99C7188CF32DA4FE8BB9684CA9886C8` |

## 3. Nhận xét dư / thiếu / conflict

Mức Cao: ảnh hưởng căn cứ/bản bàn giao; TB: có thể dẫn tới cách triển khai khác nhau hoặc chặn nhầm; Thấp: đề xuất đơn giản hóa, không phải lỗi nghiệp vụ.

| ID | Vị trí file/mục/dòng | Loại | Mức độ | Nhận xét và tác động | Đề xuất/cách kiểm chứng | Căn cứ trang/mục/US/PAY | OQ |
|---|---|---|---|---|---|---|---|
| R01-01 | BA01:1, 4, 19, 76–84; SEQ01:3, 24, 131; IDX sơ đồ:3; LOG mục SYS-PAY-01 | Conflict phiên bản / thiếu bản nguồn | Cao | File tên **v01** lại có tiêu đề **v02**, tự liên kết chính nó làm “bản trước xác nhận”, và nhiều lần viện dẫn câu hỏi của v01. File `sys-pay-01-lap-bang-thanh-toan-v02.md` không tồn tại; liên kết từ README sơ đồ và LOG tới v02 bị gãy. Không thể lấy file hiện tại làm cả bản phân tích gốc và bản sau xác nhận, hoặc truy lại đầy đủ OQ gốc chỉ qua các liên kết này. | Khôi phục hoặc định danh rõ hai bản từ bằng chứng hiện có, đồng bộ liên kết/nhãn của sơ đồ. Kiểm tra v01 không tự trỏ chính nó như bản trước và mọi liên kết v02 có đích thật; không tự tái dựng lịch sử xác nhận. | [THAM KHẢO] BA01:1–5, 17–20; LOG mục SYS-PAY-01 ghi yêu cầu giữ hai bản. RULE mục Bàn giao và nhật ký; workflow mục Giữ bản trước và sau review. Đây là lỗi quản lý tài liệu, không phải business rule TA. | — |
| R01-02 | BA01:58–59 (kích hoạt, P5), 62 (A1); SAVE01:82–87, 118–121 | Conflict nội bộ | TB | UC bao gồm mở/sửa Draft đã lưu, nhưng P5 viết tuyệt đối “không có bảng chưa Cancelled trùng hợp đồng/kỳ”. Chính Draft đang sửa cũng thỏa điều kiện bị cấm. SAVE01 đã loại trừ `paymentId`, BA01 chưa nêu ngoại lệ đó, nên người đọc có thể áp P5 và chặn mọi lần sửa không đổi kỳ. | Tách điều kiện cho tạo mới và cập nhật; với cập nhật, không tính chính bảng đang sửa vào tập trùng. Xác minh ba ca: tạo trùng bị chặn; sửa chính bảng cùng kỳ được tiếp tục; đổi sang kỳ có bảng khác bị chặn. | [ĐẶC TẢ] TA-SPEC §4.1 US-PAY-01 cho sửa Draft; §5 PAY-01, TA-PDF tr.2 theo SOURCE. [QUYẾT ĐỊNH ĐÃ XÁC NHẬN theo BA01] CREATE-01, 02, 12; SAVE01:82 đã nêu cách hiểu cần đồng bộ. | — |
| R01-03 | SEQ01:47–50, 106–122; SAVE01:47–87, 116–135; BA01:61 bước 3, 7, 9 | Thiếu mô tả validation tại lưu | TB | SEQ01 kiểm tra kỳ đúng cấu hình khi chuẩn bị ban đầu. Khi đổi kỳ, nhánh preview chỉ nói đọc nguồn phù hợp; interaction `saveDraft` không nêu kiểm tra kỳ đầu vào đúng cấu hình hợp đồng vừa đọc. Lưu là yêu cầu độc lập, nên kiểm tra ở bước mở ban đầu chưa mô tả đủ trường hợp đổi kỳ hoặc gửi dữ liệu trực tiếp. Không kết luận hệ thống đã có lỗ hổng, vì chưa có triển khai. | Nêu rõ kiểm tra kỳ/cấu hình ở save bằng dữ liệu nguồn tin cậy và nhánh từ chối tương ứng. Xác minh yêu cầu lưu chọn quý cho hợp đồng cấu hình tháng vẫn bị từ chối dù bỏ qua preview; giữ riêng OQ chồng lấn CREATE-16. | [ĐẶC TẢ] TA-SPEC §2: kỳ tháng hoặc quý tùy cấu hình hợp đồng; §4.1 US-PAY-01, TA-PDF tr.1–2 theo SOURCE. [THAM KHẢO] BA01:61 bước 3/7; RULE yêu cầu guard và validation nhất quán. Cách đặt kiểm tra phía hệ thống là [ĐỀ XUẤT KỸ THUẬT]. | CREATE-16 vẫn mở, không dùng làm đáp án cho kiểm tra loại kỳ. |
| R01-04 | SEQ01:71–72, 98, 108–117, 125–128; EDIT01:61–70; SAVE01:89–105 | Thiếu hợp đồng dữ liệu giữa preview và save | TB | `sourceBaseline` ban đầu được trả về, nhưng sau đổi kỳ/dịch vụ/bảng giá, preview đọc nguồn mới và chỉ trả “bản xem trước cập nhật”, chưa chỉ rõ baseline mới được trả/lưu ra sao. Save lại dùng baseline để nhận diện nguồn đổi. Ví dụ chuyển tháng 1 sang tháng 2: nếu vẫn giữ baseline tháng 1, khác dữ liệu có thể bị nhận nhầm thành nguồn thay đổi A9. Đây là chỗ chưa đặc tả, không khẳng định chắc chắn baseline đang được giữ sai. | Làm rõ baseline gắn với hợp đồng/kỳ/tập nguồn nào; sau lựa chọn mới hợp lệ, bản xem trước và baseline nào cùng được chuyển sang save. Xác minh đổi kỳ hợp lệ không tự gây A9 chỉ vì so hai kỳ khác nhau; nguồn đổi thật sau preview vẫn gây A9; không coi sản lượng nhập tay là baseline nguồn. | [ĐẶC TẢ] TA-SPEC §4.1, PAY-02/03, TA-PDF tr.2 theo SOURCE. [QUYẾT ĐỊNH ĐÃ XÁC NHẬN theo BA01] CREATE-08/09, KT-02. `sourceBaseline` là [ĐỀ XUẤT KỸ THUẬT], không có căn cứ trong đặc tả bắt buộc dùng chính cơ chế này. | — |
| R01-05 | BA01:32, 59 (P4), 61 bước 7/9, 76; SEQ01:81–89, 102–120; SAVE01:66–79, 109–113 | Thiếu / mơ hồ nghiệp vụ sau xác nhận | TB | CREATE-08 cho sửa sản lượng/dịch vụ, trong khi P4 và PAY-02 yêu cầu sản lượng dùng để lập đã đối soát. Chưa rõ một giá trị NVKD sửa khác nguồn được coi là đã đối soát theo căn cứ nào; dịch vụ thêm/sửa phải gắn với nguồn nào. Kiểm tra nguồn “đã đối soát” chưa tự trả lời tính hợp lệ của dữ liệu sửa tay. CREATE-05 hiện hỏi nguồn rỗng/đối soát một phần, không trực tiếp giải quyết vấn đề này. | Bổ sung câu hỏi cho người phụ trách ở mục 4, giữ quyền sửa đã ghi nhận. Sau xác nhận, nối điều kiện vào bước sửa và lưu; không tự cấm toàn bộ sửa sản lượng, cũng không tự cho mọi giá trị sửa tay hợp lệ. | [ĐẶC TẢ] TA-SPEC §2 định nghĩa sản lượng đã đối soát; §4.1 US-PAY-01; §5 PAY-02/03, TA-PDF tr.1–2 theo SOURCE. [QUYẾT ĐỊNH ĐÃ XÁC NHẬN theo BA01] CREATE-08; chưa có câu trả lời riêng cho căn cứ đối soát dữ liệu sửa tay. | R01-OQ-01; liên quan CREATE-05/08 |
| R01-06 | SEQ01:58–69 | Dư biểu diễn — đề xuất kỹ thuật | Thấp | `opt có bảng lịch sử Cancelled` chỉ chứa note, không có message/action khác. Truy vấn ngay trước chỉ tìm bảng **chưa** Cancelled, cũng không cung cấp kết quả về lịch sử. Khung này làm người đọc tưởng có nhánh kiểm tra lịch sử bắt buộc, dù hành vi đã là bỏ Cancelled khỏi kiểm tra trùng. | Có thể thay opt bằng note chung về giữ lịch sử và tạo định danh mới; chỉ thêm truy vấn lịch sử nếu có nhu cầu thực sự. Đây là lựa chọn làm gọn sơ đồ, không bắt buộc thêm xử lý. | [THAM KHẢO] BA01:29, 47, 62 A4; SEQ01:58–69. **Không có căn cứ trong đặc tả** bắt buộc truy vấn lịch sử Cancelled khi chuẩn bị bảng mới; xếp [ĐỀ XUẤT KỸ THUẬT]. TA-SPEC §4.5 US-PAY-05 chỉ nêu không dùng lại bảng đã hủy, tr.2 theo SOURCE. | — |

## 4. Câu hỏi mới để người phụ trách xem xét

ID dưới đây chỉ có hiệu lực trong báo cáo này; chưa thêm hoặc đổi OQ của BA/design.

| ID | Vị trí mọi nguồn | Loại | Mô tả | Lý do cần xác nhận | Lựa chọn | Ảnh hưởng | Trạng thái | Người/ngày/câu trả lời và tham chiếu |
|---|---|---|---|---|---|---|---|---|
| R01-OQ-01 | TA-SPEC §2, §4.1, PAY-02/03; TA-PDF tr.1–2 theo SOURCE; BA01:32 CREATE-08, :59 P4, :61 bước 7/9, :76 CREATE-05; SEQ01:81–89, 102–120; SAVE01:66–79, 109–113 | Mơ hồ | Khi NVKD sửa sản lượng hoặc thêm/đổi dịch vụ, căn cứ nào xác định dữ liệu cuối cùng vẫn đáp ứng điều kiện sản lượng đã đối soát? | Trạng thái đối soát của bản ghi nguồn có thể không chứng minh giá trị nhập tay đã được hai bên xác nhận; chưa đủ căn cứ viết validation và kết quả kiểm thử. | Làm rõ phạm vi sửa đã được xác nhận và cách liên kết với dữ liệu đối soát; hoặc quy trình xác nhận giá trị sửa do người phụ trách cung cấp. Reviewer không chọn và không tự thêm chứng từ/quy trình. | Preview, kiểm tra trước lưu, PAY-02/03 và dữ liệu dùng tính tiền. | Cần xác nhận | Chưa có câu trả lời trong nguồn đã đọc; phát hiện 07/11/2026. |

Các OQ đã được nhận diện đúng trong BA01 và sơ đồ: CREATE-05, CREATE-06, CREATE-07, CREATE-11a, CREATE-16, CREATE-17, CREATE-18. Việc đánh dấu Blocked không phải lỗi tự thân; không yêu cầu designer tự chốt gom dòng, làm tròn, dữ liệu rỗng, danh sách trường bắt buộc hoặc kỳ chồng lấn. [BA01:70–84; IDX sơ đồ:35–44]

## 5. Bao phủ và các điểm không nên báo thiếu/dư

| Yêu cầu / nội dung | Bằng chứng trong tài liệu | Kết quả trong phạm vi lần này |
|---|---|---|
| US-PAY-01: NVKD chọn hợp đồng/kỳ, sinh dòng, tính tổng và lưu Draft; được sửa Draft [TA-SPEC §4.1, tr.2] | BA01:55–64; SEQ01 chuẩn bị/preview; SAVE01 lưu; EDIT01 sửa | Có mô tả. Cần chỉnh theo R01-02..05; chưa kiểm thử trên ứng dụng. |
| PAY-01: Active, bảng giá phù hợp, duy nhất theo tháng [TA-SPEC §5, tr.2]; tháng/quý theo §2 [tr.1] | BA01 CREATE-01/02/03/04; SEQ01:37–79; SAVE01:66–87, 118–124 | Có đối chiếu quyết định bổ sung theo BA01; CREATE-16 vẫn mở. Không coi bỏ Cancelled khỏi tập trùng hoặc hỗ trợ quý là tự bịa vì BA01 đã ghi xác nhận. R01-01 ảnh hưởng truy vết bản xác nhận. |
| PAY-02: sản lượng đã đối soát [TA-SPEC §5, tr.2] | BA01 P4/E5; SEQ01:81–89; SAVE01:72–79 | Có guard; nguồn rỗng/một phần đã chặn bằng OQ. Còn R01-OQ-01 về sửa tay. |
| PAY-03: sản lượng × đơn giá tại thời điểm tính [TA-SPEC §5, tr.2] | BA01 bước 6/10; SEQ01:92–97; SAVE01:109–114; IDX sơ đồ mục Tính tiền | Có mô tả tính phía hệ thống. Gom dòng/làm tròn còn mở; không có bằng chứng kết quả số đã được kiểm thử. |
| NFR-PAY-01: audit ai/lúc nào/thay đổi gì [TA-SPEC §6, tr.3; mã NFR nội bộ] | BA01:60–64; SAVE01:116–149 | Có audit và rollback trong interaction lưu. Không báo thiếu audit chỉ vì SEQ01 dùng ref. |
| NFR-PAY-02: phản hồi ≤3 giây với <200 dòng [TA-SPEC §6, tr.3; mã NFR nội bộ] | BA01:37, 49, 64; SAVE01:151–155 | Giữ đúng <200; điểm đo được BA01 ghi nhận bổ sung. Chưa có đo kiểm; không kết luận đạt hiệu năng từ render. |
| Lưu lặp / tạo đồng thời [TA-SPEC PAY-01; BA01 CREATE-12, KT-04] | BA01 A10 và :66; SAVE01:36–45, 116–149 | Có nhận diện retry trước kiểm tra tạo mới và kiểm soát tại giao dịch. Không báo thiếu chống lặp chỉ dựa vào truy vấn ban đầu ở SEQ01. PAY-04 gốc chống **trình duyệt** trùng thuộc UC khác. |
| Chỉ đọc module nguồn [TA-SPEC §1, tr.1] | SEQ01 và các interaction chỉ đọc `PaymentSourceReader`; IDX sơ đồ mục vai trò | Phù hợp phạm vi sơ đồ, không thấy message CRUD module nguồn. Không yêu cầu giao dịch phân tán; IDX đã nêu chưa bảo đảm snapshot nguyên tử xuyên module. |
| AC dẫn xuất / kết quả thành công và lỗi của SYS-PAY-01 | BA01 các hàng hậu điều kiện, bước, A1/A4/A9/A10, E4/E5/E9/E10, NFR | Có điều kiện kiểm chứng rải trong UC, chưa có danh mục AC được đánh ID để đối chiếu ma trận đầy đủ. Không kết luận thiếu hành vi chỉ vì chưa có mã AC; chưa thể xác nhận bao phủ ma trận toàn module. |
| US-PAY-02..05, PAY-04..08 [TA-SPEC §4.2–4.5, §5, tr.2] | BA01:68 giữ ranh giới trình duyệt; sơ đồ chỉ tạo/sửa Draft | Ngoài phạm vi chức năng được giao review, trừ liên hệ Draft/Cancelled. Không yêu cầu đưa duyệt/từ chối/tự duyệt vào sơ đồ lập bảng. |
| Mâu thuẫn đúng 500 triệu, điều chỉnh Approved, Rejected/Draft [TA-SPEC §4.3 ↔ PAY-06; §4.4 ↔ PAY-05; §3 ↔ PAY-08] | Không có nhánh giải quyết các nghiệp vụ này trong SEQ01 | Không phát hiện sơ đồ SYS-PAY-01 tự chọn đáp án. Các mâu thuẫn đó vẫn cần được theo dõi ở UC tương ứng, không chốt trong lần review này. |

Các lifeline TO-BE, `requestId`, `sourceBaseline`, `expectedVersion` không tự động là phần dư: IDX đã nêu mục đích và giới hạn; chúng phục vụ lưu lặp, phát hiện nguồn đổi và tránh ghi đè bản đã sửa. Reviewer không yêu cầu bỏ chỉ vì TA không đặt tên cơ chế. Cách tách interaction lưu bằng `ref` cũng hợp lý với hai luồng tạo/sửa. [THAM KHẢO: BA01 KT-02/04; IDX sơ đồ:18–33; SEQ01:125–129; SAVE01; EDIT01]

## 6. Lệnh kiểm chứng và kết quả

Thực hiện bằng PowerShell; Java **27.0.1.0.3**, PlantUML **1.2024.3** từ extension `jebbs.plantuml-2.18.1`. Không đo hiệu năng hoặc chạy thử quy trình nghiệp vụ trên ứng dụng.

```powershell
$reviewJar = 'C:/Users/phong/.vscode/extensions/jebbs.plantuml-2.18.1/plantuml.jar'
$reviewFiles = @(Get-ChildItem docs/design/payment-management/diagrams -Filter 'sequence-sys-pay-01-*.puml' -File | ForEach-Object { $_.FullName })
java '-Djava.awt.headless=true' -jar $reviewJar -charset UTF-8 -checkonly @reviewFiles
$reviewPreview = Join-Path $env:TEMP 'qtkd-ai-review-01-sequence'
New-Item -ItemType Directory -Force -Path $reviewPreview | Out-Null
java '-Djava.awt.headless=true' '-DPLANTUML_LIMIT_SIZE=16000' -jar $reviewJar -charset UTF-8 -tpng -failfast2 -o $reviewPreview @reviewFiles
git diff --check
```

- Cú pháp: **PASS**, exit code 0 cho cả ba PUML.
- Kết xuất PNG: **PASS**, exit code 0 cho cả ba PUML; ảnh tại `%TEMP%/qtkd-ai-review-01-sequence/`. Đã xem ảnh sơ đồ lập mới, nhãn tiếng Việt và các khung được kết xuất; chưa kiểm tra trực quan chi tiết hai ảnh lưu/sửa. Không tạo ảnh cạnh nguồn thiết kế.
- Kiểm tra đích liên kết Markdown bằng PowerShell: **FAIL** với liên kết v02 ở README sơ đồ và prompt-log; `Test-Path` xác nhận file v02 không tồn tại. Hai interaction PUML được tham chiếu có thật. BA01 tự trỏ chính nó làm bản trước: R01-01.
- `git diff --check`: **PASS** ở thời điểm kiểm tra đầu vào; kiểm tra lại báo cáo sau ghi. Lệnh này không kiểm tra nội dung file untracked; đã kiểm tra riêng khoảng trắng và bảng/liên kết của báo cáo.
- Đối chiếu nội dung: thủ công theo bảng mục 3/5. Đây là bằng chứng review tài liệu; các tình huống trong cột cách kiểm chứng là đề nghị cho lần sửa/kiểm thử tiếp theo, chưa phải ca kiểm thử đã chạy.

## 7. Nhật ký và bàn giao

Ghi nhật ký ngay trong báo cáo để giữ giới hạn reviewer chỉ tạo báo cáo mới. Không sửa LOG, OQ, thiết kế, phân tích hoặc báo cáo đánh giá của nhóm.

- Công cụ: Codex trong chat hiện tại; phiên bản ứng dụng/model cụ thể không được cung cấp. Tool đọc/kiểm chứng: PowerShell, `rg`, Git, Java/PlantUML và trình xem ảnh.
- Skill đã đọc: graphify. Không có `graphify-out/graph.json`, nên không có kết quả truy vấn graph được dùng làm căn cứ; không tạo graph ngoài phạm vi review. Đã đọc hướng dẫn PDF khi kiểm tra khả năng truy cập nguồn, nhưng không có kết quả trích xuất PDF được dùng.
- Prompt thực tế, giữ nguyên nội dung yêu cầu và chỉ chuẩn hóa đường dẫn liên kết:

> thực hiện review [sys-pay-01-lap-bang-thanh-toan-v01.md](../../analysis/payment-management/sys-pay-01-lap-bang-thanh-toan-v01.md), tìm điểm dư/thiếu/conflict
>
> review thêm [sequence-sys-pay-01-lap-bang-thanh-toan.puml](../../design/payment-management/diagrams/sequence-sys-pay-01-lap-bang-thanh-toan.puml)

- Đầu ra AI: duy nhất `docs/review/payment-management/ai-review-01.md`; không tạo commit. Nguồn/bản đầu vào và hash ở mục 2; kiểm chứng ở mục 6.
- Phần nhóm sửa/phê duyệt: chưa có ghi nhận trong lần review này. Các nhận xét chưa được AI tự phân loại Đúng/Sai/Thừa thay nhóm.
- Bàn giao: người phụ trách đánh giá R01-01..06; xác nhận R01-OQ-01 và các CREATE còn mở; sau đó giao design cập nhật phần được chấp nhận, giữ bản trước/sau. Trạng thái thiết kế tiếp tục **Design Pending Approval** theo footer SEQ01/SAVE01/EDIT01.
