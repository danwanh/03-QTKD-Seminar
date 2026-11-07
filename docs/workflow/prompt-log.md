# Nhật ký prompt – thiết lập workspace

SETUP-01 và SETUP-02 ghi lại các lần thiết lập trước. Cấu hình hiện tại đã được
hợp nhất thành một file AGENTS.md trong SETUP-03; không dùng cấu trúc cũ để chạy.

## SETUP-01 – 07/11/2026

- Công cụ: Codex desktop; CLI dùng kiểm tra bộ nạp: `codex-cli 0.166.0-alpha.5.1`.
- Chế độ: một chat thiết lập workspace; không chạy agent nghiệp vụ hoặc review
  thiết kế chưa tồn tại.
- Trích yêu cầu người dùng, chuẩn hóa xuống dòng; phần tham chiếu trực tuyến
  đã lược bỏ theo yêu cầu điều chỉnh SETUP-02:

> hãy Thiết lập các agent phục vụ phân tích, thiết kế, review cho workspace này;
> viết rules yêu cầu AI bám đặc tả, chỉ rõ nguồn, không tự chốt nghiệp vụ chưa rõ.
> Viết hướng dẫn chạy và tổng hợp cấutrúc workspace. Kiểm tra cấu hình thực sự
> sử dụng được trong công cụ nhóm chọn. Với phạm vi theo bt TA 1-2,
> [Phần tham chiếu tài liệu nghiệp vụ trực tuyến đã lược bỏ.]
> Yêu cầu đầu ra: .cursor/agents/; .cursor/rules/; README.md hướng dẫn sử dụng
> hoặc đầu ra tương đương

- Nguồn nghiệp vụ hiện áp dụng: TA-PDF và TA-SPEC cục bộ theo
  [sổ nguồn](../requirements/payment-management/sources.md). Cấu hình và code
  demo hiện có dùng khảo sát; tài liệu chính thức chỉ hướng dẫn định dạng công cụ.
- Làm rõ công cụ: người dùng trả lời “tương đương, tức là có thể sử dụng cấu hình
  codex/claude”. Không diễn giải câu này thành phê duyệt nghiệp vụ.
- Đầu ra ban đầu (đã thay ở SETUP-03): rules, ba vai trò, cấu hình riêng theo
  công cụ, README, scripts kiểm tra, tài liệu workflow và sổ nguồn.
  Không sửa nội dung TA-SPEC hay mã nguồn ứng dụng.
- Kiểm chứng: xem [config-verification.md](config-verification.md).
- Nhóm sửa/phê duyệt: chưa có ghi nhận trong lần chạy này; nhóm bổ sung sau.

## SETUP-02 – 07/11/2026

- Yêu cầu người dùng: chỉnh lại cấu hình, bỏ qua các đường dẫn tới tài liệu
  nghiệp vụ trực tuyến.
- Thực hiện: loại đường dẫn, mã nguồn tham khảo, tab và nội dung đối chiếu
  trực tuyến khỏi sổ nguồn/hướng dẫn/nhật ký; cập nhật rules, agent và bộ sinh
  adapter để chỉ dùng TA-SPEC/TA-PDF cục bộ làm căn cứ nghiệp vụ.
- Phần tham chiếu trực tuyến trong SETUP-01 đã được lược bỏ theo yêu cầu này;
  không trình bày bản trích ở trên là toàn văn prompt ban đầu.
- Kiểm chứng bản điều chỉnh: xem [config-verification.md](config-verification.md).

## SETUP-03 – 07/11/2026

- Yêu cầu người dùng: “hãy merge lại tất cả thành 1 file dùng chung, bỏ việc
  tách ra như cursor, codex claude”.
- Thực hiện: gộp rules, hướng dẫn ba/design/reviewer và các nguyên tắc làm việc
  chung vào AGENTS.md; bỏ cấu hình riêng, các file vai trò/rules rời và bộ sinh.
- Cách dùng: mọi công cụ đọc cùng AGENTS.md rồi đóng vai theo prompt;
  reviewer dùng chat mới. README và tài liệu workflow phản ánh cấu trúc này.
- Công cụ kiểm tra được sửa để kiểm tra file chung, nguồn cục bộ, liên kết
  và nội dung thực sự được bộ nạp nhận. Không coi các vai trò là custom agent
  đã đăng ký riêng theo công cụ.
- Kiểm chứng hiện tại: [config-verification.md](config-verification.md).

## Những lần chạy tiếp theo

Dùng bảng ở [workflow README](README.md); thêm prompt thực tế, kết quả,
nguồn/bản thiết kế đầu vào và phần nhóm sửa. Các prompt mẫu trong README gốc
chưa phải bằng chứng đã chạy BA/design/reviewer.

## SYS-PAY-01 – 07/11/2026

- Công cụ: Codex trong phiên chat hiện tại; phiên bản ứng dụng không được cung cấp. Thực hiện trực tiếp yêu cầu biên soạn tài liệu phân tích, không chạy subagent hoặc reviewer độc lập.
- Prompt thực tế của người dùng (giữ nguyên phần yêu cầu, không chép trạng thái IDE):

> bổ sung đặc tả vào analyis/sys-pay-01-lap-bang-thanh-toan-v02.md. đay là bảng cuối sau khi đã chốt các điểm chưa hợp lý. trình bày phần đã xác nhận, đã đề xuất trước, sau đó mới thực hiện spec system.
>
> analyis/sys-pay-01-lap-bang-thanh-toan-v01.md. là spec phân tích yêu cầu từ đề, bao gồm luồng gốc từ yêu cầu, phân tích, các điểm mơ hồ cần xác định.

- Nguồn đã đọc: AGENTS.md; TA-SPEC §1–6; sổ nguồn; mẫu `docs/analysis/payment-management/sys-pay-03-duyet-tu-choi.md`; hướng dẫn workflow; các câu trả lời CREATE-… và lời đồng ý phương án trong cùng cuộc trao đổi. Không trích xuất lại TA-PDF; số trang được dẫn theo sổ nguồn. Các file rules rời trong ngữ cảnh IDE không còn tồn tại; áp dụng AGENTS.md hợp nhất hiện có.
- Đầu ra AI viết:
  - [v01](../analysis/payment-management/sys-pay-01-lap-bang-thanh-toan-v01.md): Use Case theo đề, phân tích và 13 câu hỏi gốc; không áp dụng ngược các quyết định bổ sung.
  - [v02](../analysis/payment-management/sys-pay-01-lap-bang-thanh-toan-v02.md): ghi nhận quyết định người dùng, phương án đã đồng ý trước bảng Use Case, các nhánh thay thế/lỗi, NFR và chi tiết còn mở. Giữ ID CREATE-…; không tự đóng câu hỏi chưa có câu trả lời cụ thể.
- Kiểm chứng: kiểm tra bằng PowerShell các mục bắt buộc của mẫu, số cột bảng Markdown, liên kết file cục bộ, ký tự lỗi UTF-8, khoảng trắng cuối dòng và tham chiếu `Blocked by CREATE-…`: **PASS cho cả hai file**. `git diff --check`: **PASS**. Lần thử kiểm tra bằng `python` không chạy được vì lệnh không có trong PATH; đã dùng PowerShell thay thế. Đã đối chiếu nhánh gửi lại yêu cầu với kiểm tra trùng, thêm thứ tự xử lý để không chặn nhầm yêu cầu đã lưu thành công.
- Chưa kiểm chứng: chưa có ứng dụng thực thi để đo SLA 3 giây, kiểm thử giao dịch/chống lặp/phân quyền; không tuyên bố triển khai đã đạt. Không tạo commit, không sửa TA-SPEC, SYS-PAY-03 hoặc mã nguồn.
- Phần người dùng xác nhận: các câu trả lời và phương án ở Phần 1–2 của v02; người xác nhận là người dùng trong chat, ngày ghi nhận 07/11/2026. Phần nhóm chỉnh sửa trực tiếp trong hai file: chưa có ghi nhận ở lần này.

## SYS-PAY-01-SEQUENCE – 07/11/2026

- Công cụ: Codex trong phiên chat hiện tại; phiên bản ứng dụng không được cung cấp. Biên soạn sơ đồ trực tiếp, không chạy subagent/reviewer độc lập.
- Prompt thực tế của người dùng:

> thiết kế sequence diagram vào design/payment-management/diagrams/ định dạng puml.

- Đầu vào đã đọc: AGENTS.md; TA-SPEC; SYS-PAY-01 v02 (quyết định, KT, luồng, OQ); chỉ mục thiết kế; bốn file hiện trạng `src/Qtkd.Api/Program.cs`, `Services/ContractService.cs`, `Models/Contract.cs`, `Qtkd.Api.csproj`. Hiện trạng chỉ có demo hợp đồng, không coi các lifeline thanh toán là code đã tồn tại. Không trích xuất lại PDF hoặc truy cập nguồn nghiệp vụ trực tuyến.
- Đầu ra AI: ba file PUML lập mới, sửa Draft, lưu Draft dùng chung; [danh mục và truy vết](../design/payment-management/diagrams/README.md); cập nhật chỉ mục thiết kế để dẫn đến sơ đồ thực có. Các thành phần, phương thức, requestId, baseline nguồn, kiểm tra phiên bản là đề xuất TO-BE; quy tắc nghiệp vụ dẫn v02. Không sửa v01/v02, TA-SPEC hoặc mã nguồn.
- Kiểm chứng: PlantUML 1.2024.3, Java 27.0.1.0.3; `-checkonly` và `-tpng -failfast2` với UTF-8: **PASS cả ba file**. Đã xem ảnh, sửa nhãn điều kiện bị parser hiểu thành hyperlink và tăng chiều rộng message; render lại thành công, không còn image map hyperlink ngoài ý muốn. Nhánh từ chối sửa nằm ngoài opt để kết thúc interaction trước bước ghi. Danh sách lệnh/kết quả nằm trong README sơ đồ. Lần đầu ghép `-checkonly -failfast2` phát sinh ảnh cạnh nguồn; đã dọn đúng 6 PNG/image map được tạo và chạy lại `-checkonly` riêng thành công.
- Kiểm tra bổ sung: cấu trúc PUML, ref đến interaction có thật, mã CREATE so với v02, liên kết chỉ mục và khoảng trắng: **PASS**; `git diff --check`: **PASS**. Ảnh preview nằm tại `%TEMP%/qtkd-sys-pay-01-sequence-preview-final/`, không đưa vào nguồn thiết kế.
- Chưa kiểm chứng: chưa chạy ứng dụng để đo 3 giây hoặc kiểm thử transaction/idempotency/quyền; chưa chốt gom dòng, làm tròn, trường bắt buộc và các câu hỏi còn mở của v02. Không tạo kết quả kiểm thử nghiệp vụ giả.
- Phần nhóm sửa/phê duyệt: chưa có ghi nhận cho các sơ đồ mới. Trạng thái **Design Pending Approval**; phần người dùng đã xác nhận của v02 vẫn giữ nguyên.
