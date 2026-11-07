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
