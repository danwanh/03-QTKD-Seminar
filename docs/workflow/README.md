# Quy trình và minh chứng sử dụng AI – TA 1–2

Tài liệu này chuẩn bị cách làm cho nhóm, không tuyên bố đã có thiết kế/review/
slide. Phạm vi lần thiết lập hiện tại: agent, rules, hướng dẫn và kiểm chứng.
Sản phẩm cuối bài tập được liệt kê ở TA-PDF trang 3, xem [sổ nguồn](../requirements/payment-management/sources.md).

## Trình tự

1. Kiểm tra cấu hình theo [README workspace](../../README.md); mở chat mới để
   nạp hướng dẫn. Ghi công cụ/phiên bản và nguồn đầu vào.
2. Chạy BA từ TA-SPEC/TA-PDF cục bộ; nhóm kiểm tra OQ. Không tự suy ra câu trả
   lời từ tài liệu ngoài phạm vi.
3. Chạy design lần đầu; ghi giả định/OQ ngay từ đầu, không sửa hồi tố đặc tả.
4. **Giữ bản lần đầu trước khi sửa** bằng một trong hai cách bên dưới.
5. Mở chat mới chạy reviewer từ nguồn gốc và bản thiết kế, giữ nguyên báo cáo AI.
6. Nhóm phân loại từng nhận xét Đúng/Sai/Thừa và ghi căn cứ. Người phụ trách
   xác nhận OQ nếu đủ thông tin; AI không tự nhận vai người phê duyệt.
7. Giao design cập nhật theo phần được chấp nhận; kiểm tra UML/API/data/truy vết,
   ghi bản sau review và nội dung thay đổi.
8. Tổng hợp prompt, phân công, báo cáo đánh giá và tối đa 5 slide theo đề.

## Giữ bản trước và sau review

Không ghi đè bản duy nhất. Chọn một cách, ghi trong nhật ký:

- **Git:** nhóm tự kiểm tra thay đổi và commit thiết kế lần đầu; ghi commit ID
  vào nhật ký. Sau review, commit bản cập nhật và ghi commit ID thứ hai.
  Không dùng `git add .` thiếu kiểm tra vì workspace có tài liệu đầu vào khác.
- **Thư mục riêng:** trước khi sửa, sao chép đầy đủ
  `docs/design/payment-management/` sang
  `docs/design-snapshots/payment-management/first-run/`; sau sửa sao chép sang
  `docs/design-snapshots/payment-management/after-review/`. Giữ cả sơ đồ và ma
  trận, không chỉ ảnh. Không ghi đè snapshot cũ nếu đã tồn tại; thêm số lần/ngày.

Các đường dẫn snapshot trên là vị trí dự kiến, chỉ tạo khi có bản cần lưu.
Lần thiết lập cấu hình không tự tạo commit hay bản thiết kế giả.

## Nhật ký prompt

Ghi vào [prompt-log.md](prompt-log.md). Không lưu mật khẩu/token hoặc dữ liệu
không liên quan. Prompt dài có thể lưu file trong `docs/workflow/prompts/` và
dẫn đường dẫn; phải giữ bản thực tế đã gửi, không chỉ prompt mẫu.

| Lần/ngày | Công cụ/phiên bản, chế độ vai trò/subagent | Vai trò/người thao tác | Prompt thực tế | Nguồn/bản đầu vào | Đầu ra/commit | Đã kiểm tra và kết quả | Phần nhóm sửa |
|---|---|---|---|---|---|---|---|

## Open Questions và quyết định

BA giữ bảng tại `docs/analysis/payment-management/open-questions.md`.
Design dẫn ID của BA; nếu phát hiện thêm, ghi trong Open Questions của bản
tóm tắt thiết kế và bàn giao để nhóm hợp nhất. Reviewer chỉ dẫn OQ, không sửa bảng.

| ID | Vị trí nguồn, các phía mâu thuẫn | Loại Mâu thuẫn/Mơ hồ/Thiếu | Mô tả | Lý do cần xác nhận | Lựa chọn nếu có | Ảnh hưởng | Trạng thái | Người/ngày/câu trả lời và tham chiếu |
|---|---|---|---|---|---|---|---|---|

Không có trả lời có căn cứ thì giữ Cần xác nhận. “Reviewer AI đồng ý” hoặc
“tham khảo có cách làm này” không phải bằng chứng phê duyệt nghiệp vụ.

## Đánh giá AI Reviewer của nhóm

Khi đã có review, nhóm tạo `docs/review/payment-management/review-assessment.md`:

| ID nhận xét AI | Đúng/Sai/Thừa | Lý do, nguồn đặc tả và vị trí | Chấp nhận/từ chối/chờ xác nhận | Thay đổi thiết kế, file/commit | Người/ngày đánh giá |
|---|---|---|---|---|---|

Phân biệt: nhận xét đúng có căn cứ; nhận xét sai hiểu nhầm nguồn/thiết kế;
nhận xét thừa ngoài phạm vi hoặc chỉ là sở thích kỹ thuật. Nhận xét phụ thuộc OQ
chưa trả lời phải giữ trạng thái chờ, không bịa kết luận để hoàn thành bảng.

## Phần AI viết và phần nhóm sửa

Lần thiết lập này do AI tạo/cập nhật bộ agent/rules, các adapter, README, công cụ
kiểm tra, sổ nguồn và minh chứng. Nguồn có sẵn: đặc tả, tài liệu đồ án, Excel,
code demo. `CLAUDE.md` giữ hướng dẫn chung cũ và thêm điểm vào dự án.
Người dùng xác nhận cho phép dùng cấu hình Codex/Claude tương đương; điều đó
không phải xác nhận tất cả nội dung cấu hình hoặc câu hỏi nghiệp vụ.

Nhóm ghi thay đổi thực tế, không nhận phần việc chưa làm:

| File/mục | Phần AI tạo/đề xuất | Phần nhóm kiểm tra/sửa | Lý do | Người/ngày | Minh chứng diff/commit |
|---|---|---|---|---|---|

Nhóm bổ sung bảng phân công tại workspace, gồm người phụ trách, công việc,
sản phẩm bàn giao và người kiểm tra. Chỉ ghi thông tin đã được nhóm xác nhận;
không tự gán người phụ trách hoặc nhận đã hoàn thành phần việc khác.
