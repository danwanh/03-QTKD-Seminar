# Sequence diagram — SYS-PAY-01: Lập bảng thanh toán

Trạng thái: **Design Pending Approval**. Nguồn nghiệp vụ: [TA-SPEC §1, §2, §4.1, PAY-01..03, §6](../../../requirements/payment-management/spec.md). Quyết định bổ sung và câu hỏi mở: [SYS-PAY-01 v02, Phần 1–4](../../../analysis/payment-management/sys-pay-01-lap-bang-thanh-toan-v02.md). Số trang PDF theo sổ nguồn, không trích xuất lại PDF trong lần này.

## Danh mục tương tác

| File | Nội dung | Truy vết v02 |
|---|---|---|
| [sequence-sys-pay-01-lap-bang-thanh-toan.puml](sequence-sys-pay-01-lap-bang-thanh-toan.puml) | Chuẩn bị bảng mới, đọc nguồn, kiểm tra trùng, sinh dòng và xem trước; tham chiếu tương tác lưu. | Bước 1–8; A4; E4, E5, E10; CREATE-01..04, 08; KT-01, KT-03. |
| [sequence-sys-pay-01-sua-draft.puml](sequence-sys-pay-01-sua-draft.puml) | Mở Draft của người lập, kiểm tra quyền/trạng thái/hiệu lực, chỉnh sửa và tính lại; tham chiếu tương tác lưu. | A1; E9; CREATE-03, 08, 10; KT-01. |
| [sequence-sys-pay-01-luu-draft.puml](sequence-sys-pay-01-luu-draft.puml) | Lưu mới/cập nhật, nhận diện retry trước kiểm tra trùng, nguồn đổi cần xác nhận, giao dịch bảng/dòng/audit/kết quả thao tác, xung đột và rollback. | Bước 8–11; A9, A10; E4, E5, E9, E10; KT-02, KT-04, KT-05; NFR-PAY-01, 02. |

`ref` biểu diễn một interaction dùng chung, không phải gọi một dịch vụ khác. Luồng lập/sửa cần đi tiếp sang sơ đồ lưu mới tạo ra dữ liệu bền vững. Việc chuẩn bị bản xem trước chưa ghi bảng Draft vào kho lưu trữ. [AC dẫn xuất] [v02 bước 7–10]

## Hiện trạng và các vai trò thiết kế

Đã đọc `src/Qtkd.Api/Program.cs`, `Services/ContractService.cs`, `Models/Contract.cs` và `Qtkd.Api.csproj`. Hiện trạng là API demo hợp đồng dùng `ConcurrentDictionary`, chưa có module bảng thanh toán, bảng giá/sản lượng, audit, cơ sở dữ liệu giao dịch hoặc phân quyền NVKD. Model hợp đồng có Active nhưng chưa có trường hết hạn; không coi prototype là nghiệp vụ đã hoàn thiện. Các lifeline và phương thức dưới đây đều là **[ĐỀ XUẤT KỸ THUẬT]**, chưa có trong code và chưa phải API contract được duyệt.

| Lifeline | Trách nhiệm trong sơ đồ | Lý do / lựa chọn khác |
|---|---|---|
| PaymentForm | Thu nhận thao tác, giữ bản xem trước và hiển thị kết quả/đối chiếu nguồn. | Phù hợp thao tác NVKD ở v02; không quyết định quyền hoặc thành tiền cuối cùng. |
| PaymentApplicationService | Điều phối kiểm tra, tính tiền, nhận diện lưu lặp và lệnh ghi. | Một vai trò điều phối đủ cho UC; chưa cần bổ sung lớp controller/domain service riêng chỉ để vẽ sơ đồ. |
| PaymentSourceReader | Vai trò đọc hợp đồng, bảng giá và sản lượng từ các module khác. | Gom các tương tác chỉ đọc vào một lifeline để sơ đồ dễ theo dõi. Có thể triển khai bằng các interface riêng; không bắt buộc xây module nguồn mới hoặc gộp ba module hiện có. Không có message ghi dữ liệu nguồn. [TA-SPEC §1] |
| PaymentStore | Vai trò lưu bảng, dòng, audit và kết quả thao tác trong một giao dịch cục bộ; kiểm soát điều kiện tại điểm ghi. | Đáp ứng v02 KT-04. Không coi kiểm tra SELECT trước ghi là đủ; công nghệ và cách thực thi ràng buộc thuộc LLD. Không dùng giao dịch phân tán lên nguồn. |

## Lựa chọn kỹ thuật và giới hạn

- **Nhận diện thao tác lưu:** `requestId` ràng buộc người thực hiện, loại thao tác và nội dung; retry giữ nguyên định danh/nội dung, thay đổi nghiệp vụ là thao tác mới. Chỉ vô hiệu hóa nút Lưu không đủ cho mất phản hồi hoặc yêu cầu đồng thời. Kết quả thao tác và dữ liệu nghiệp vụ phải cùng commit để có thể trả lại kết quả đã lưu. Không trả kết quả của người khác hoặc tái sử dụng mã cho nội dung khác. Đây là phương án đề xuất để đáp ứng CREATE-12/KT-04, chưa chốt dùng HTTP header hay công nghệ cụ thể.
- **Kiểm tra phiên bản:** đề xuất `expectedVersion` khi sửa để phát hiện dữ liệu đã đổi trong phiên khác. Kiểm tra người lập/Draft và tính duy nhất tại thời điểm ghi vẫn là bắt buộc theo v02; chỉ kiểm tra khi mở màn hình không đủ. [CREATE-10, CREATE-12; A1; E9; KT-04]
- **Đối chiếu nguồn:** `sourceBaseline` là mốc của dữ liệu nguồn dùng cho bản xem trước, tách biệt phần NVKD chỉnh sửa. So sánh nguồn mới với baseline, không so trực tiếp sản lượng NVKD sửa với nguồn rồi coi đó là nguồn thay đổi. Khi nguồn thực sự đổi, trình bày tác động và yêu cầu xác nhận trước khi tính lại; không âm thầm ghi đè. Baseline được giữ bởi hệ thống hoặc được xác thực, không tin dữ liệu nguồn/giá do trình duyệt tự khai. Cách dùng mã phiên bản hoặc so sánh dữ liệu phụ thuộc interface nguồn, chưa có trong prototype. [CREATE-08, CREATE-09; KT-01, KT-02]
- **Tính nhất quán với module nguồn:** sơ đồ đọc lại nguồn trước khi ghi và giao dịch cục bộ cho dữ liệu thanh toán. Không tuyên bố có thể khóa nguồn hoặc bảo đảm snapshot nguyên tử xuyên ba module. Thiết kế chi tiết phải xác định khả năng cung cấp mốc/phiên bản nguồn; không suy diễn API nguồn đã hỗ trợ. [TA-SPEC §1; v02 bước 9; KT-04]
- **Lỗi đọc kho lưu trữ:** mọi truy vấn kho thất bại phải kết thúc thao tác với E10, không được hiểu lỗi truy vấn là “không có bảng trùng”, “không có kết quả lưu lặp” hoặc “không tìm thấy bảng”. Các message trả dữ liệu trong sơ đồ là nhánh truy vấn thành công; lỗi kỹ thuật dùng quy tắc E10/KT-04. Kiểm tra thời hạn tại điểm ghi dựa trên thông tin hiệu lực nguồn vừa đọc; không khẳng định prototype đã có ngày hết hạn. [CREATE-03; v02 E10; KT-04]
- **Tính tiền:** hệ thống tính lại trước lưu, không lấy thành tiền trình duyệt làm kết quả cuối. Cách gom dòng/làm tròn còn Blocked by CREATE-06, CREATE-07. Không tự thêm VAT, chiết khấu hoặc trạng thái mới. [PAY-03; v02 Phần 4]

## Câu hỏi còn mở được giữ nguyên

| ID | Giới hạn của sơ đồ |
|---|---|
| CREATE-05 | Không tự chọn cho lập rỗng, lập một phần hay chặn toàn bộ khi đối soát một phần; luồng chính dành cho dữ liệu đủ điều kiện. |
| CREATE-06, CREATE-07 | Message sinh dòng/tính tiền là thao tác ở mức thiết kế, chưa chốt thuật toán gom dòng/làm tròn. |
| CREATE-11a | Có kiểm tra trường bắt buộc nhưng chưa bịa danh sách trường hoặc tự bắt buộc ghi chú. |
| CREATE-16 | Kiểm tra trùng chính xác hợp đồng/kỳ; chưa tự áp dụng quy tắc cấm các kỳ khác nhau nhưng chồng lấn. |
| CREATE-17 | Giữ lệnh cấm thao tác sau hết hiệu lực; không tự cho ngoại lệ khi đối soát muộn. |
| CREATE-18 | Chỉ thiết kế tạo/sửa Draft, không tự lan cập nhật nguồn hoặc quyền thao tác sang PendingApproval/Approved. |

## Kiểm chứng

Đã kiểm tra ngày 07/11/2026 bằng PlantUML **1.2024.3** trong extension `jebbs.plantuml-2.18.1`, Java **27.0.1.0.3**:

| Kiểm tra | Kết quả |
|---|---|
| `-checkonly`, UTF-8 | PASS cho cả 3 file. |
| Kết xuất PNG bằng `-tpng -failfast2` | PASS cho cả 3 file; ảnh ở thư mục tạm, không thêm ảnh sinh tự động vào nguồn thiết kế. |
| Kiểm tra ảnh | Đã xem các ảnh để kiểm tra chữ tiếng Việt, nhãn điều kiện, bố cục và khung alt/opt/loop/break/ref; sửa lỗi điều kiện bị hiểu thành hyperlink và tăng chiều rộng message để tránh xuống dòng quá nhiều. |
| Liên kết, interaction ref, mã CREATE | PASS; tham chiếu đến file thật, mã câu hỏi giữ theo v02. |
| `git diff --check` và kiểm tra khoảng trắng file PUML mới | PASS. |

Lệnh đã dùng, chạy từ gốc workspace:

```powershell
$taskJar = 'C:/Users/phong/.vscode/extensions/jebbs.plantuml-2.18.1/plantuml.jar'
$taskFiles = @(Get-ChildItem docs/design/payment-management/diagrams -Filter 'sequence-sys-pay-01-*.puml' -File | ForEach-Object { $_.FullName })
java '-Djava.awt.headless=true' -jar $taskJar -charset UTF-8 -checkonly @taskFiles
$taskPreview = Join-Path $env:TEMP 'qtkd-sys-pay-01-sequence-preview-final'
New-Item -ItemType Directory -Force -Path $taskPreview | Out-Null
java '-Djava.awt.headless=true' '-DPLANTUML_LIMIT_SIZE=16000' -jar $taskJar -charset UTF-8 -tpng -failfast2 -o $taskPreview @taskFiles
```

SLA 3 giây và cơ chế giao dịch/chống lặp là yêu cầu thiết kế, chưa được đo/kiểm thử trên ứng dụng. Kết xuất thành công không đồng nghĩa nghiệp vụ hoặc thiết kế đã được người phụ trách phê duyệt.

Trong phiên bản PlantUML này, chạy kèm `-checkonly -failfast2` đã phát sinh ảnh cạnh nguồn; đã dọn đúng các ảnh/image map do lần kiểm tra tạo ra. Lệnh kiểm tra riêng ở trên dùng `-checkonly`, lệnh render dùng `-failfast2` và đích thư mục tạm.
