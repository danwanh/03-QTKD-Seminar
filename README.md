# QTKD Seminar – workspace Bảng thanh toán TA 1–2

Workspace phục vụ phân tích đặc tả, thiết kế và review bằng AI cho module
Bảng thanh toán. Công cụ dùng để kiểm chứng trong lần thiết lập này là **Codex**;
có adapter cho **Claude Code** và **Cursor**. Người dùng đã xác nhận chấp nhận
cấu hình Codex/Claude tương đương đầu ra `.cursor/` của đề.

Phạm vi công việc hiện tại là thiết lập agent/rules/hướng dẫn và kiểm chứng cấu
hình theo yêu cầu người dùng và đề TA 1–2 trong workspace.
Các thư mục thiết kế/review là nơi nhận sản phẩm ở bước tiếp theo, chưa phải một
bộ thiết kế hoàn chỉnh. Code demo hợp đồng đã có phục vụ khảo sát hiện trạng.

## Bắt đầu

1. Mở **thư mục gốc này** trong công cụ, không chỉ mở một file con.
2. Đọc [sổ nguồn](docs/requirements/payment-management/sources.md) và
   [đặc tả TA](docs/requirements/payment-management/spec.md).
3. Với Codex, tạo chat mới trong workspace để nạp [AGENTS.md](AGENTS.md).
   Với Claude Code, [CLAUDE.md](CLAUDE.md) nhập `@AGENTS.md`.
4. Chạy kiểm tra cấu hình trong terminal tại thư mục gốc, cần Python **3.11+**,
   không cần cài thư viện Python ngoài:

   ```sh
   python3 scripts/sync_agent_config.py --check
   python3 scripts/verify_agent_config.py
   ```

5. Nếu đã có Codex CLI, kiểm tra bộ nạp thực tế:

   ```sh
   codex --version
   python3 scripts/verify_agent_config.py --codex
   ```

   Bước này dùng `codex debug prompt-input`, không gọi model, không in toàn bộ
   prompt/cấu hình cá nhân. Nếu phiên bản CLI không có lệnh debug hoặc không được
   phép tạo dữ liệu phiên cục bộ, dùng bước kiểm tra trong chat bên dưới và ghi
   đúng giới hạn. Không tắt cơ chế quyền truy cập để vượt lỗi.

Kết quả và giới hạn của lần chạy thực tế:
[config-verification.md](docs/workflow/config-verification.md).

## Các agent

| Vai trò | Đọc/làm gì | Được ghi đầu ra |
|---|---|---|
| `ba` | Phân tích 5 US, 8 PAY, 2 NFR, AC và Open Questions | `docs/analysis/payment-management/` |
| `design` | Khảo sát AS-IS, thiết kế HLD/LLD, UML, API, dữ liệu, truy vết | `docs/design/payment-management/` |
| `reviewer` | Đọc đặc tả và thiết kế độc lập; phát hiện suy diễn/thiếu/bất nhất | Báo cáo mới trong `docs/review/payment-management/` |

Agent không được tự xác nhận nghiệp vụ, sửa đặc tả hay triển khai mã nguồn.
Giới hạn ghi file là hướng dẫn hành vi; không phải quyền hệ điều hành riêng cho
từng thư mục. Quyền thực tế do phiên công cụ/người dùng kiểm soát.

### Cách dùng được trên Codex và Claude

Gọi vai trò bằng ngôn ngữ tự nhiên trong chat. `AGENTS.md` chỉ tới file hướng dẫn
gốc; với chế độ này **không cần** cơ chế custom subagent của phiên bản công cụ.
Đây là đổi vai trò trong chat hiện tại, không tự tạo phiên AI khác.

Kiểm tra nạp hướng dẫn trước khi chạy nghiệp vụ:

```text
Chỉ kiểm tra cấu hình, không ghi file. Nêu hai file rules bắt buộc,
nguồn đặc tả TA 1–2, file hướng dẫn của ba/design/reviewer và giới hạn mỗi vai trò.
Đọc các file đó, không đoán theo tên thư mục. Nếu đúng 500 triệu thì có thể
chốt ngay người duyệt không? Dẫn hai vị trí trong đề và nêu cách xử lý.
```

Chạy BA:

```text
Đóng vai agent ba. Đọc đặc tả Bảng thanh toán TA 1–2 và sổ nguồn.
Phân tích đủ US-PAY-01..05, PAY-01..08 và hai NFR; ghi kết quả trong
docs/analysis/payment-management/ theo hướng dẫn vai trò.
Mỗi điểm chưa rõ phải có OQ, vị trí nguồn và lý do cần xác nhận; không tự chốt.
```

Chạy design sau khi có đầu vào BA hoặc xác định rõ phần BA còn thiếu:

```text
Đóng vai agent design. Thiết kế lần đầu module Bảng thanh toán theo đặc tả TA
và đầu ra BA hiện có. Khảo sát src/Qtkd.Api/ trước khi mô tả AS-IS.
Tạo các tài liệu và PlantUML trong docs/design/payment-management/.
Giữ các OQ còn mở; phần phụ thuộc phải đánh dấu Blocked by OQ, không tự chọn
phương án nghiệp vụ. Ghi rõ bước kiểm chứng đã chạy/chưa chạy.
```

Mở **chat mới** cho reviewer, chỉ cung cấp đường dẫn nguồn và bản cần review:

```text
Đóng vai agent reviewer. Đọc độc lập đặc tả TA 1–2 và toàn bộ bản thiết kế
trong docs/design/payment-management/. Kiểm tra truy vết, nhất quán, suy diễn,
phạm vi và các OQ. Ghi báo cáo mới ai-review-<NN>.md trong thư mục review.
Không sửa thiết kế, không tự đóng câu hỏi nghiệp vụ. Nếu thiếu đầu vào thì nêu rõ.
```

Sau review, **nhóm** đánh giá từng nhận xét Đúng/Sai/Thừa, trả lời OQ khi có căn
cứ và giao design sửa phần đã thống nhất. AI không tự ký duyệt thay nhóm.

### Custom subagent của từng công cụ

| Công cụ | Điểm vào rules | Nơi đăng ký native agent | Cách gọi |
|---|---|---|---|
| Codex | `AGENTS.md` yêu cầu đọc `.agents/rules/` | `.codex/agents/*.toml` | Yêu cầu rõ “Ủy nhiệm cho subagent ba/design/reviewer…” nếu phiên bản hỗ trợ |
| Claude Code | `CLAUDE.md` nhập `AGENTS.md` | `.claude/agents/*.md` | Kiểm tra `/agents`, rồi yêu cầu subagent theo tên |
| Cursor | `.cursor/rules/*.mdc`, `alwaysApply: true` | `.cursor/agents/*.md` | Yêu cầu Agent dùng subagent theo tên |

Codex TOML khai báo `name`, `description`, `developer_instructions`; không ép
model hay thay quyền của phiên. Agent Markdown có `name`, `description`,
`model: inherit`. Reviewer được phép ghi báo cáo nên không gắn chế độ cấm mọi
ghi file; giới hạn không sửa thiết kế nằm trong prompt.

Các file `.agents/agents/*.md` tự chúng **không** đăng ký subagent cho Codex/
Claude. `.cursor/rules` phải dùng `.mdc`; một file `.md` đặt ở đó không phải
project rule hợp lệ. Không dùng lệnh `--agent` hay slash command tự đặt khi
chưa kiểm tra phiên bản công cụ. Nếu chưa có native agent, dùng cách đổi vai trò
trong chat ở trên và ghi rõ chế độ đã dùng.

Sau khi đổi adapter, mở lại phiên/chat để công cụ nạp lại. Claude Code cho phép
kiểm tra danh sách agent bằng `/agents`; Cursor kiểm tra mục Rules/Agents trong
cài đặt dự án. Việc nhìn thấy file hoặc parse đúng chưa chứng minh model đã
tuân thủ hành vi; cần dùng các prompt kiểm tra ở phần minh chứng.

## Rules cốt lõi

- Đề gốc [TA-PDF](docs/requirements/payment-management/assignment-ta-1-2.pdf)
  và bản chép `spec.md` cục bộ là nguồn nghiệp vụ cho TA. Bỏ qua đường dẫn tới
  tài liệu nghiệp vụ trực tuyến; agent không dùng chúng để bổ sung yêu cầu.
- Mỗi kết luận dẫn trang/mục/US/PAY. Tách yêu cầu gốc, tham khảo, đề xuất kỹ
  thuật, giả định cần xác nhận và quyết định có người xác nhận.
- Mâu thuẫn/mơ hồ/thiếu → OQ + lý do + ảnh hưởng; không tự chọn cách hiểu.
  Ví dụ: đúng 500 triệu, sửa Approved, Rejected/Draft, kỳ tháng/quý.
- Chỉ đọc hợp đồng/bảng giá/sản lượng; không mở rộng CRUD hay ký điện tử,
  phát hành, VAT từ đồ án tổng thể vào bài này.
- Truy vết đủ 5 US, 8 PAY, hai NFR. Giữ đúng ≤3 giây với **dưới 200 dòng**.
- Không tuyên bố đã render/test/phê duyệt khi chưa có bằng chứng.

Chi tiết: [quy tắc chung](.agents/rules/qtkd-context.md) và
[quy tắc module](.agents/rules/payment-management.md).

## Cấu trúc workspace

```text
.
├── AGENTS.md                        # Điểm vào Codex, điều phối vai trò
├── CLAUDE.md                        # Điểm vào Claude, nhập AGENTS.md
├── .agents/
│   ├── agents/{ba,design,reviewer}.md # Nguồn hướng dẫn dùng chung
│   └── rules/{qtkd-context,payment-management}.md
├── .codex/agents/*.toml              # Adapter native Codex, sinh tự động
├── .claude/agents/*.md               # Adapter Claude Code, sinh tự động
├── .cursor/
│   ├── agents/*.md                  # Adapter Cursor, sinh tự động
│   └── rules/*.mdc                  # Always Apply, sinh tự động
├── docs/
│   ├── requirements/
│   │   ├── payment-management/{spec.md,sources.md,assignment-ta-1-2.pdf}
│   │   ├── QTKD_DATH.pdf            # Bối cảnh đồ án rộng
│   │   └── BA_QTKD_User_Stories.xlsx # Phân tích đồ án đã có
│   ├── analysis/payment-management/ # Đầu ra BA, hiện chờ chạy
│   ├── design/payment-management/   # Đầu ra design, hiện có chỉ mục
│   │   └── diagrams/               # PlantUML class/sequence/state/component
│   ├── review/payment-management/   # Review AI và đánh giá của nhóm
│   ├── workflow/                    # Quy trình, nhật ký, minh chứng cấu hình
│   └── api-demo.http                # Request cho demo hợp đồng đã có
├── scripts/
│   ├── sync_agent_config.py         # Sinh adapter/kiểm tra đồng bộ
│   ├── verify_agent_config.py       # Kiểm tra nguồn, cấu hình, bộ nạp Codex
│   └── demo-api.{sh,ps1}            # Script demo hợp đồng đã có
└── src/Qtkd.Api/                    # ASP.NET Core .NET 8, demo hợp đồng
```

Danh mục tài liệu thiết kế dự kiến:
[docs/design/payment-management/README.md](docs/design/payment-management/README.md).
Quy trình prompt, bản lần đầu/sau review và mẫu đánh giá:
[docs/workflow/README.md](docs/workflow/README.md).

## Bảo trì cấu hình

Chỉ sửa nguồn trong `.agents/agents/` và `.agents/rules/`, sau đó chạy:

```sh
python3 scripts/sync_agent_config.py
python3 scripts/sync_agent_config.py --check
python3 scripts/verify_agent_config.py
```

Script sinh các adapter và báo sai lệch; không xóa file lạ của người dùng.
Bộ kiểm tra sẽ báo adapter lạ để người phụ trách quyết định. Frontmatter của
nguồn dùng giá trị đơn: chuỗi có dấu ngoặc kép kiểu JSON, boolean, hoặc tên
đơn giản; muốn thêm cấu trúc YAML phức tạp cần cập nhật bộ đọc trước.
Checksum bảo vệ bản PDF/đặc tả đã đối chiếu; thay nguồn có chủ đích phải ghi
quyết định và cập nhật giá trị kiểm tra sau khi đối chiếu, không chỉ sửa để pass.

## Chạy code demo hiện có (tùy chọn)

Cần .NET 8 SDK. Tại thư mục gốc:

```sh
dotnet run --project src/Qtkd.Api --urls http://localhost:5080
```

Mở [docs/api-demo.http](docs/api-demo.http) để gọi API. `scripts/demo-api.sh` và
`.ps1` là demo đã có. Đây là API hợp đồng lưu bộ nhớ, chưa triển khai Bảng thanh
toán. Lần thiết lập agent này không coi demo là sản phẩm đã đạt yêu cầu TA và
không kiểm thử ứng dụng khi không sửa mã ứng dụng.

## Tài liệu chính thức đã đối chiếu

- [Codex: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
  và [custom subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).
- [Claude Code: project instructions/import](https://code.claude.com/docs/en/memory)
  và [subagents](https://code.claude.com/docs/en/sub-agents).
- [Cursor: rules](https://cursor.com/docs/rules) và
  [subagents](https://cursor.com/docs/subagents).

Ngày đối chiếu: 07/11/2026. Cấu hình đúng định dạng không đồng nghĩa đã chạy
thực tế trên mọi công cụ; xem trạng thái kiểm chứng riêng trong minh chứng.
