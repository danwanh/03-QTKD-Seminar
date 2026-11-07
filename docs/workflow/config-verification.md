# Kiểm chứng cấu hình agent/rules

Ngày: 07/11/2026 (Asia/Ho_Chi_Minh). Công cụ kiểm chứng: Codex; người dùng
đã xác nhận chấp nhận cấu hình Codex/Claude tương đương đầu ra Cursor.

## Kết quả đã chạy

| Kiểm tra | Kết quả thực tế | Bằng chứng/phạm vi |
|---|---|---|
| Công cụ hiện có | Codex CLI `0.166.0-alpha.5.1` | Đã chạy `codex --version` |
| Đồng bộ adapter | PASS | `python3 scripts/sync_agent_config.py --check`, exit 0; 11 adapter khớp nguồn |
| Cấu trúc, frontmatter, TOML, đường dẫn | PASS | `python3 scripts/verify_agent_config.py`, exit 0, không có check thất bại |
| Nguồn đặc tả/PDF | PASS | SHA-256 đúng; TA-SPEC không bị sửa, bản sao PDF nguyên byte |
| Bộ nạp Codex thực | PASS | `python3 scripts/verify_agent_config.py --codex`, exit 0; nhận đúng nội dung AGENTS.md của workspace và tham chiếu cả hai rules |
| Đăng ký custom agent Codex thực | PASS | Trong metadata công cụ của prompt, trường `agent_type` có tên và mô tả của ba native agent `ba`, `design`, `reviewer` |
| Whitespace của thay đổi Git | PASS | `git diff --check`, exit 0 |
| Claude Code/Cursor | Kiểm tra cấu trúc, chưa chạy runtime | Máy không có CLI/app tương ứng trong lần kiểm tra; không tuyên bố đã nạp thành công trên hai công cụ này |
| Hành vi model/thiết kế/review nghiệp vụ | Chưa chạy | Lần này kiểm tra cấu hình và bộ nạp, không gọi model khác hoặc tạo bộ thiết kế/review |

Trích kết quả thật từ lần kiểm tra bộ nạp:

```text
INFO: codex-cli 0.166.0-alpha.5.1
PASS: Codex real prompt loader ran
PASS: Codex loaded this project's AGENTS.md
PASS: Codex received both rule references
PASS: Codex exposes native agent_type inventory
PASS: Codex discovered native agent: ba
PASS: Codex discovered native agent: design
PASS: Codex discovered native agent: reviewer
INFO: Project guidance and native agent registration verified; no model call or business-agent execution was performed.
RESULT: PASS (0 failed checks)
```

Kiểm tra native agent dựa trên metadata **công cụ thực** của Codex, không chỉ
tìm chữ “ba/design/reviewer” trong README hay AGENTS.md. Nội dung rules/role
được agent đọc theo chỉ dẫn trong AGENTS.md và developer_instructions của adapter;
phép kiểm tra này không tự chứng minh mọi lần model sẽ tuân thủ hành vi.

Không có raw prompt/cấu hình cá nhân được ghi vào repository. Bộ nạp Codex cần
quyền truy cập dữ liệu phiên cục bộ; trong phiên thiết lập đã chạy lại với quyền
được công cụ cho phép. Script không thay quyền, cấu hình tài khoản hay model.

## Những điểm cấu hình đã sửa so với đầu vào

- BA trước đây chỉ đọc tài liệu đồ án tổng thể và yêu cầu ghi Excel; nay đọc
  đúng đặc tả TA và có đầu ra BA/OQ riêng, giữ Excel đồ án có sẵn.
- Rules trước đây nhắc `docs/business-rules.md` không tồn tại; thay bằng sổ
  nguồn cục bộ, phân biệt đặc tả TA với tài liệu đồ án tổng thể.
- `CLAUDE.md` trước đây chưa nhập AGENTS.md như mô tả; nay có `@AGENTS.md`.
- Bổ sung adapter native đúng định dạng Codex/Claude/Cursor; `.agents/` vẫn
  là nguồn dùng chung, có kiểm tra phát hiện lệch giữa các bản.
- Nêu đúng trạng thái thư mục thiết kế: mới có chỉ mục, chưa có bộ thiết kế.

## Kiểm chứng bản điều chỉnh SETUP-02 – 07/11/2026

- Đã bỏ đường dẫn, mã nguồn tham khảo, tab và nội dung đối chiếu nghiệp vụ
  trực tuyến trong cấu hình, sổ nguồn, README và nhật ký. Rà soát workspace
  hiện tại không còn các tham chiếu đã loại bỏ.
- Rules và adapter Codex chỉ định TA-SPEC/TA-PDF cục bộ làm nguồn nghiệp vụ;
  bộ sinh đã cập nhật 9 adapter bị ảnh hưởng, đủ 11 adapter đồng bộ: PASS.
- Đã chạy lại `python3 scripts/verify_agent_config.py --codex`: PASS, exit 0,
  không có check thất bại; Codex vẫn nạp AGENTS.md và nhận đủ ba native agent.
- SHA-256 của đặc tả và PDF vẫn đúng; đường dẫn cục bộ trong tài liệu hợp lệ.
  `git diff --check`: PASS. Chưa chạy model nghiệp vụ hoặc runtime Claude/Cursor.

## Lệnh tái kiểm tra

```sh
python3 scripts/sync_agent_config.py --check
python3 scripts/verify_agent_config.py
python3 scripts/verify_agent_config.py --codex
```

Python 3.11+, không cần thư viện ngoài. Lệnh cuối yêu cầu Codex CLI có
`debug prompt-input`; không gửi yêu cầu tới model, không in prompt cá nhân.

## Kiểm tra hành vi khi chạy agent thật

Các prompt sau là kịch bản kiểm tra, chưa được coi đã chạy nếu chưa lưu output:

| Vai trò | Prompt kiểm tra không ghi file | Tiêu chí đạt |
|---|---|---|
| ba | Đúng 500.000.000 đồng thì ai duyệt? Chỉ trả lời trong chat, dẫn nguồn. | Dẫn §4.3 và PAY-06, ghi mâu thuẫn/cần xác nhận; không tự chọn KTT/GĐKD |
| design | Theo đề TA có thể chốt ngay sửa trực tiếp Approved không? Chỉ dùng đặc tả cục bộ, không ghi file. | Giữ §4.4/PAY-05 thành OQ, trình bày phương án có nhãn nếu cần, không tự chọn cách hiểu |
| reviewer | Review bộ thiết kế hiện chưa có đủ tài liệu. Không ghi file. | Báo thiếu đầu vào, không tự tạo nhận xét cho tài liệu không tồn tại hoặc sửa thiết kế |

Nên chạy reviewer trong chat mới. Khi thử native subagent, cần yêu cầu ủy nhiệm
rõ ràng và lưu thông tin công cụ thực sự dùng agent nào; đổi vai trò trong chat
không phải bằng chứng native subagent đã chạy.
