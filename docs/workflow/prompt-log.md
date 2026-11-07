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

## SETUP-04 – 07/11/2026

- Công cụ: Claude Code (desktop app, tab Code), model Claude Opus 5.5.
- Yêu cầu người dùng: “đọc src code và đề bạn hãy giúp tôi tạo các file skill để
  làm sys spec, sequence, các diagram, thiết kế dữ liệu, ma trận truy vết”.
- Làm rõ: người dùng chọn đặt skill ở `skills/` trung lập (không dùng thư mục
  cấu hình riêng theo công cụ, giữ nguyên hướng gộp của SETUP-03).
- Nguồn đã đọc: TA-SPEC, sổ nguồn, AGENTS.md, README, workflow, `sys-pay-03-duyet-tu-choi.md`,
  toàn bộ `src/Qtkd.Api/` (4 file). Không đọc DATH/Excel; không mở PDF (dùng TA-SPEC).
- Đầu ra: `skills/README.md`, `skills/_shared/payment-context.md`, 5 skill
  (sys-spec, uml-diagrams, sequence-diagram, data-design, traceability-matrix);
  thêm cách gọi skill trong AGENTS.md/README; verify script kiểm tra skill.
  Không chạy skill nào để tạo đặc tả/thiết kế; không sửa đặc tả hay `src/`.
- Kiểm chứng: xem [config-verification.md](config-verification.md).
- Nhóm sửa/phê duyệt: chưa có ghi nhận.

## Những lần chạy tiếp theo

Dùng bảng ở [workflow README](README.md); thêm prompt thực tế, kết quả,
nguồn/bản thiết kế đầu vào và phần nhóm sửa. Các prompt mẫu trong README gốc
chưa phải bằng chứng đã chạy BA/design/reviewer.

## BA-01 – 07/11/2026

- Công cụ: Claude Code CLI, model Claude Opus 5.5; vai trò BA trong chat hiện tại.
- Prompt (nội dung):

> Đọc đặc tả US-PAY-03 trong BAITAP_TA_1-2.pdf và business rule, tìm những điểm
> mâu thuẫn, mơ hồ hoặc thiếu thông tin, chỗ nào chưa rõ cần xác nhận lại và kèm lý do.

- Nguồn: TA-PDF (BAITAP_TA_1-2.pdf), TA-SPEC `spec.md`, rules trong AGENTS.md.
- Đầu ra: 11 điểm cần xác nhận OQ-P03-01..11 (vị trí trong đề, loại, lý do, lựa chọn),
  hiện ở `docs/analysis/payment-management/can-xac-nhan.md` mục 1.
- Đã kiểm tra: đối chiếu nguyên văn §3, §4.3, PAY-04..08, §6 với TA-SPEC. Chưa có xác nhận nghiệp vụ.

## BA-02 – 07/11/2026

- Công cụ: Claude Code CLI, model Claude Opus 5.5; vai trò BA trong chat hiện tại.
- Prompt thực tế (đề xuất cho OQ-P03-12..18 theo thứ tự), kèm yêu cầu "đè lên bản v2":

> - chỉ người tạo, Rejected được hủy trực tiếp
> - đề xuất
> - người cụ thể
> - Trưởng kế toán
> - đề xuất
> - có, số hiệu
> - đề xuất

- Thực hiện: cập nhật trực tiếp `sys-pay-03-duyet-tu-choi-v2.md` (không tạo v3; bản v2 trước đó chưa commit nên không còn lưu).
  OQ-P03-12, 14, 15, 17 gắn `[ĐỀ XUẤT NHÓM]`; OQ-P03-13, 16, 18 ("đề xuất") do AI đề xuất, gắn nhãn mới `[ĐỀ XUẤT AI]`, chờ nhóm chấp nhận.
  Phát sinh OQ-P03-19..21.
- Lưu ý: đề xuất 12 thêm chuyển `Rejected → Cancelled` ngoài §3/US-PAY-05; đề xuất 14 có thể mâu thuẫn với đề xuất 07 (ghi OQ-P03-19).

## BA-03 – 07/11/2026

- Công cụ: Claude Code CLI, model Claude Opus 5.5; vai trò BA trong chat hiện tại.
- Prompt thực tế:

> docs\analysis\payment-management\sys-pay-03-duyet-tu-choi.md viet muc 1 dac ta muc 2 la diem de xuat
> Toi muon viet lai
> can-xac-nhan.md: gom nhung van de mo ho, can xac nhan
> sys-pay-03-...-v1: gom dac ta sau khi co nhung de xuat, va liet ke cac de xuat

- Thực hiện:
  - `sys-pay-03-duyet-tu-choi.md` → `sys-pay-03-duyet-tu-choi-v1.md` (git mv): Mục 1 đặc tả đã áp dụng đề xuất, Mục 2 bảng 21 đề xuất kèm vị trí trong đề.
  - `can-xac-nhan.md` viết lại: chỉ gồm vấn đề cần xác nhận (OQ-P03-01..11 từ đề, OQ-P03-12..21 phát sinh), có vị trí, loại, lý do, lựa chọn.
- Bản đặc tả lần đầu (chưa có đề xuất) còn trong git, commit `9c11cc7`.

## BA-04 / DESIGN-01 – 07/11/2026

- Công cụ: Claude Code CLI, model Claude Opus 5.5; trong chat hiện tại.
- Prompt thực tế:

> bo cot khac voi cau chu de va ap dung trong muc 1
> va tao puml cho cho sys-pay-03 luu trong design/, co swimlane, day du cac luong chinh va luong thay the

- Thực hiện:
  - `sys-pay-03-duyet-tu-choi-v1.md`: bỏ 2 cột "Khác với câu chữ đề", "Áp dụng trong Mục 1" ở bảng Mục 2.
  - Tạo `docs/design/payment-management/diagrams/sys-pay-03-activity.puml`: activity diagram 4 swimlane
    (Người duyệt, Hệ thống, Nhân viên kinh doanh, Kế toán trưởng nhận thông báo), gồm dòng cơ bản 1–9 và A1, A3, A3.2, A4–A7.
- Chưa kiểm tra kết xuất sơ đồ (máy không có Java/PlantUML).
