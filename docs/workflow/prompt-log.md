# Nhật ký prompt – thiết lập workspace

## SETUP-01 – 07/11/2026

- Công cụ: Codex desktop; CLI dùng kiểm tra bộ nạp: `codex-cli 0.166.0-alpha.5.1`.
- Chế độ: một chat thiết lập workspace; không chạy agent nghiệp vụ hoặc review
  thiết kế chưa tồn tại.
- Yêu cầu người dùng (nội dung giữ nguyên, chuẩn hóa xuống dòng):

> hãy Thiết lập các agent phục vụ phân tích, thiết kế, review cho workspace này;
> viết rules yêu cầu AI bám đặc tả, chỉ rõ nguồn, không tự chốt nghiệp vụ chưa rõ.
> Viết hướng dẫn chạy và tổng hợp cấutrúc workspace. Kiểm tra cấu hình thực sự
> sử dụng được trong công cụ nhóm chọn. Với phạm vi theo bt TA 1-2,
> https://docs.google.com/document/d/1I_IshVHK8r2lkjtv5ekD5JQV4SRdI44MbvJ8ouGZlis/edit?tab=t.wacxj1o2c65v
> đây là link tham khảo nghiệp vụ và user story.
> Yêu cầu đầu ra: .cursor/agents/; .cursor/rules/; README.md hướng dẫn sử dụng
> hoặc đầu ra tương đương

- Nguồn: file PDF người dùng đính kèm, TA-SPEC hiện có, các tab Google Docs đã
  đọc trong [sổ nguồn](../requirements/payment-management/sources.md), cấu hình
  và code demo hiện có; tài liệu chính thức về định dạng cấu hình công cụ.
- Làm rõ công cụ: người dùng trả lời “tương đương, tức là có thể sử dụng cấu hình
  codex/claude”. Không diễn giải câu này thành phê duyệt nghiệp vụ.
- Đầu ra: `.agents/`, `.codex/agents/`, `.claude/agents/`, `.cursor/`,
  `AGENTS.md`, điểm vào `CLAUDE.md`, `README.md`, scripts kiểm tra, tài liệu workflow
  và sổ nguồn. Không sửa nội dung TA-SPEC hay mã nguồn ứng dụng.
- Kiểm chứng: xem [config-verification.md](config-verification.md).
- Nhóm sửa/phê duyệt: chưa có ghi nhận trong lần chạy này; nhóm bổ sung sau.

## Những lần chạy tiếp theo

Dùng bảng ở [workflow README](README.md); thêm prompt thực tế, kết quả,
nguồn/bản thiết kế đầu vào và phần nhóm sửa. Các prompt mẫu trong README gốc
chưa phải bằng chứng đã chạy BA/design/reviewer.
