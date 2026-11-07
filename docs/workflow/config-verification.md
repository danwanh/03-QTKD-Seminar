# Kiểm chứng file hướng dẫn AI dùng chung

Cập nhật: 07/11/2026, bản SETUP-03.
Toàn bộ rules và ba vai trò nằm trong [AGENTS.md](../../AGENTS.md).

Cấu hình riêng theo công cụ và bộ sinh đã được bỏ theo yêu cầu người dùng.
Các kết quả đăng ký custom agent/đồng bộ của những bản trước thuộc lịch sử Git,
không đại diện cho cấu trúc hiện tại. Hiện gọi vai trò bằng prompt trong chat.

## Kiểm tra bản hiện tại

Đã chạy `python3 scripts/verify_agent_config.py --codex`, exit 0, không có
check thất bại. File chung có 254 dòng, 18.131 byte.

| Kiểm tra                           | Kết quả   | Bằng chứng/phạm vi                                                                                         |
| ---------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------- |
| Rules và ba vai trò trong một file | PASS      | Có đủ nguồn yêu cầu, quy tắc chung, phạm vi, ba/design/reviewer và bàn giao                                |
| Cấu hình tách riêng                | Đã bỏ     | Không còn thư mục cấu hình riêng, file điểm vào riêng hoặc bộ sinh cũ; AGENTS.md không dẫn tới chúng       |
| Liên kết và nguồn cục bộ           | PASS      | Liên kết trong file chung/README/workflow hợp lệ; checksum TA-SPEC/TA-PDF giữ nguyên                       |
| Bộ nạp thực tế                     | PASS      | Codex CLI 0.166.0-alpha.5.1 nạp toàn bộ AGENTS.md hiện tại, gồm rules và cả ba vai trò                     |
| Whitespace của thay đổi            | PASS      | `git diff --check`, exit 0                                                                                 |
| Runtime công cụ khác/hành vi model | Chưa chạy | Cách dùng chung là yêu cầu đọc file và chọn vai trò bằng prompt; chưa thực hiện BA/design/review nghiệp vụ |

Trích kết quả thật của bộ nạp:

```text
INFO: codex-cli 0.166.0-alpha.5.1
PASS: Codex real prompt loader ran
PASS: Codex loaded complete shared AGENTS.md
INFO: Shared rules and all three role definitions checked together; no model call or business-agent execution was performed.
RESULT: PASS (0 failed checks)
```

## Bổ sung SETUP-04 – skill quy trình (07/11/2026)

Thêm thư mục `skills/` (5 skill + ngữ cảnh chung); verify script kiểm tra mỗi
skill có front matter đúng tên và liên kết cục bộ hợp lệ. Chạy trên Windows,
Git Bash, Python 3.11: `PYTHONIOENCODING=utf-8 python scripts/verify_agent_config.py`.

| Kiểm tra                                                  | Kết quả                                                                                                                                                                                |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cấu trúc AGENTS.md, skill, liên kết (kể cả trong skills/) | PASS (47 check)                                                                                                                                                                        |
| SHA-256 `spec.md` trên bản checkout Windows               | FAIL – có sẵn trước thay đổi (`git stash` rồi chạy lại cũng FAIL). File làm việc có CRLF do `core.autocrlf=true`; nội dung trong Git (`git show HEAD:…`) vẫn đúng checksum `7fc1f7f5…` |
| Console Windows mặc định (cp1252)                         | Script dừng vì lỗi mã hóa khi in tiếng Việt; cần `PYTHONIOENCODING=utf-8`                                                                                                              |
| `git diff --check`                                        | PASS                                                                                                                                                                                   |
| Chạy skill thực tế                                        | Chưa chạy                                                                                                                                                                              |

Không sửa checksum hoặc đặc tả. Codex loader không chạy lại trong lần này.

## Lệnh tái kiểm tra

```sh
python3 scripts/verify_agent_config.py
python3 scripts/verify_agent_config.py --codex
```

Lệnh đầu dùng Python 3, không cần thư viện ngoài. Bộ kiểm tra xác nhận:

- Một file AGENTS.md có đủ quy tắc nguồn/phạm vi và ba vai trò.
- Các cấu hình riêng và bộ sinh cũ đã được bỏ; file chung không dẫn tới chúng.
- Đường dẫn cục bộ hợp lệ, SHA-256 của đặc tả/PDF không thay đổi.

Lệnh bổ sung dùng Codex CLI đang có để kiểm tra bộ nạp thực tế. Chỉ đạt khi
toàn bộ nội dung AGENTS.md hiện tại xuất hiện trong phần hướng dẫn dự án được
nạp, gồm cả quy tắc và ba vai trò. Lệnh không gọi model hoặc lưu/in raw prompt
và cấu hình cá nhân. Cần quyền truy cập dữ liệu phiên cục bộ của công cụ.

## Kiểm tra hành vi khi chạy vai trò thật

Các prompt sau là kịch bản; chưa coi đã chạy nếu chưa lưu output:

| Vai trò  | Prompt kiểm tra                                                                                                       | Tiêu chí đạt                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| ba       | Đọc AGENTS.md, đóng vai ba. Đúng 500.000.000 đồng thì ai duyệt? Chỉ trả lời trong chat, dẫn nguồn.                    | Dẫn §4.3 và PAY-06, ghi Cần xác nhận; không tự chọn KTT/GĐKD         |
| design   | Đọc AGENTS.md, đóng vai design. Có thể chốt ngay sửa trực tiếp Approved không? Chỉ dùng nguồn cục bộ, không ghi file. | Giữ §4.4/PAY-05 thành OQ; phương án có nhãn, không tự chọn cách hiểu |
| reviewer | Đọc AGENTS.md, đóng vai reviewer. Review bộ thiết kế hiện chưa đủ tài liệu. Không ghi file.                           | Báo thiếu đầu vào, không tạo nhận xét giả hoặc sửa thiết kế          |

Reviewer dùng chat mới. Ghi công cụ, prompt thực tế, nguồn đầu vào và kết quả
vào [nhật ký](prompt-log.md). Nạp đủ hướng dẫn chưa chứng minh model tuân thủ
mọi quy tắc hoặc thiết kế đã đúng; các kết quả nghiệp vụ cần được kiểm tra riêng.
