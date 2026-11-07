# QTKD Seminar – workspace Bảng thanh toán TA 1–2

Toàn bộ quy tắc và ba vai trò AI nằm trong một file dùng chung:
[AGENTS.md](AGENTS.md). Mọi công cụ sử dụng cùng file này và cùng cách gọi vai trò
bằng prompt. Chỉnh hướng dẫn trực tiếp trong file, sau đó mở chat mới để đọc lại.

Nguồn nghiệp vụ là [đặc tả TA](docs/requirements/payment-management/spec.md) và
[PDF đề bài](docs/requirements/payment-management/assignment-ta-1-2.pdf) cục bộ.
[Sổ nguồn](docs/requirements/payment-management/sources.md) ghi vị trí trang/mục.
Các đường dẫn tới tài liệu nghiệp vụ trực tuyến được bỏ qua.

Phạm vi công việc hiện tại là thiết lập hướng dẫn AI và kiểm chứng. Các thư mục
thiết kế/review đang chờ đầu ra nghiệp vụ; chưa có bộ thiết kế hoàn chỉnh.

## Cách dùng thống nhất

Mở thư mục gốc workspace, yêu cầu AI đọc toàn bộ AGENTS.md rồi chọn vai trò:

| Vai trò | Công việc | Nơi ghi đầu ra |
|---|---|---|
| ba | Phân tích 5 US, 8 PAY, 2 NFR, AC và Open Questions | docs/analysis/payment-management/ |
| design | Khảo sát AS-IS, HLD/LLD, UML, API, dữ liệu, truy vết | docs/design/payment-management/ |
| reviewer | Review độc lập, dẫn nguồn và ghi vấn đề | docs/review/payment-management/ |

Prompt mở đầu dùng được trong mọi công cụ có khả năng đọc file workspace:

```text
Đọc toàn bộ AGENTS.md ở gốc workspace và áp dụng quy tắc trong file.
Nêu nguồn đặc tả, ba vai trò và giới hạn ghi file trước khi làm.
Chỉ dùng TA-SPEC/TA-PDF cục bộ làm căn cứ nghiệp vụ.
```

Việc tự nạp file phụ thuộc công cụ/phiên bản; prompt yêu cầu đọc file ở trên là
cách dùng chung. Nếu công cụ không đọc được workspace, đính kèm chính AGENTS.md
và các nguồn cục bộ cần dùng, đồng thời kiểm tra AI đã đọc được nội dung.

### Phân tích

```text
Đọc AGENTS.md và đóng vai agent ba. Phân tích đủ US-PAY-01..05, PAY-01..08
và hai NFR trong đặc tả TA 1–2. Ghi kết quả tại docs/analysis/payment-management/
theo phần Vai trò ba. Mỗi điểm chưa rõ phải có OQ, nguồn và lý do cần xác nhận;
không tự chốt nghiệp vụ.
```

### Thiết kế

```text
Đọc AGENTS.md và đóng vai agent design. Thiết kế lần đầu module Bảng thanh toán
từ đặc tả TA và đầu ra BA nếu có. Khảo sát src/Qtkd.Api/ trước khi mô tả AS-IS.
Ghi tài liệu và PlantUML tại docs/design/payment-management/ theo phần Vai trò
design. Giữ OQ còn mở; phần phụ thuộc ghi Blocked by OQ. Ghi kiểm chứng đã chạy/
chưa chạy và giữ bản lần đầu trước khi sửa sau review.
```

### Review trong chat mới

```text
Đọc AGENTS.md và đóng vai agent reviewer. Đọc độc lập đặc tả TA và bản thiết kế
tại docs/design/payment-management/. Kiểm tra truy vết, nhất quán, suy diễn,
phạm vi và OQ. Ghi báo cáo mới ai-review-<NN>.md theo phần Vai trò reviewer.
Không sửa thiết kế hoặc tự đóng OQ. Thiếu đầu vào thì báo rõ danh sách thiếu.
```

Đây là ba vai trò trong chat theo hướng dẫn chung. Sau review, nhóm đánh giá
từng nhận xét Đúng/Sai/Thừa, xác nhận nghiệp vụ khi đủ căn cứ và giao design
cập nhật phần được chấp nhận. AI không tự phê duyệt thay nhóm.

## Kiểm tra cấu hình

Cần Python 3, không cài thư viện ngoài:

```sh
python3 scripts/verify_agent_config.py
```

Bộ kiểm tra xác nhận file chung có đủ rules/ba/design/reviewer, không còn cấu
hình tách riêng, các liên kết cục bộ hợp lệ và checksum nguồn không thay đổi.
Để kiểm tra thêm bộ nạp thực tế bằng Codex CLI đang dùng trong workspace:

```sh
python3 scripts/verify_agent_config.py --codex
```

Lệnh bổ sung dùng bộ nạp cục bộ, không gọi model hoặc in prompt/cấu hình cá nhân.
Kết quả và giới hạn: [config-verification.md](docs/workflow/config-verification.md).
Việc nạp được hướng dẫn chưa chứng minh model luôn tuân thủ hoặc thiết kế đã đúng.

Prompt kiểm tra không ghi file:

```text
Đọc AGENTS.md. Không ghi file. Nếu bảng có đúng 500.000.000 đồng, có thể chốt
ngay ai duyệt không? Dẫn hai vị trí trong đặc tả và nêu cách xử lý.
```

Kết quả cần nêu mâu thuẫn giữa §4.3 và PAY-06, ghi Cần xác nhận và lý do;
không tự chọn KTT/GĐKD. Các kịch bản khác nằm trong minh chứng kiểm tra.

## Cấu trúc workspace

```text
.
├── AGENTS.md                        # File quy tắc và ba vai trò dùng chung
├── README.md                        # Hướng dẫn sử dụng
├── docs/
│   ├── requirements/
│   │   ├── payment-management/{spec.md,sources.md,assignment-ta-1-2.pdf}
│   │   ├── QTKD_DATH.pdf            # Bối cảnh đồ án tổng thể
│   │   └── BA_QTKD_User_Stories.xlsx # Phân tích đồ án đã có
│   ├── analysis/payment-management/ # Đầu ra BA
│   ├── design/payment-management/   # Đầu ra thiết kế, hiện có chỉ mục
│   │   └── diagrams/               # PlantUML
│   ├── review/payment-management/   # Review AI và đánh giá của nhóm
│   ├── workflow/                    # Quy trình, prompt, minh chứng
│   └── api-demo.http                # Request demo hợp đồng
├── scripts/
│   ├── verify_agent_config.py       # Kiểm tra file chung và nguồn
│   └── demo-api.{sh,ps1}            # Demo hợp đồng đã có
└── src/Qtkd.Api/                    # ASP.NET Core .NET 8, demo hợp đồng
```

Danh mục thiết kế dự kiến:
[docs/design/payment-management/README.md](docs/design/payment-management/README.md).
Cách lưu prompt, bản trước/sau review, đánh giá AI và phần nhóm sửa:
[docs/workflow/README.md](docs/workflow/README.md).

## Bảo trì

Sửa quy tắc và vai trò trực tiếp trong AGENTS.md; chạy bộ kiểm tra ở trên.
Khi đổi nguồn có chủ đích, đối chiếu lại PDF/đặc tả và ghi quyết định trước khi
cập nhật checksum trong công cụ kiểm tra. Không sửa checksum chỉ để kiểm tra đạt.

Code demo hiện có cần .NET 8 SDK, chạy từ thư mục gốc:

```sh
dotnet run --project src/Qtkd.Api --urls http://localhost:5080
```

Dùng [docs/api-demo.http](docs/api-demo.http) để gọi API. Demo hợp đồng lưu trong
bộ nhớ chưa triển khai Bảng thanh toán; không coi đó là kết quả đã đạt yêu cầu TA.
