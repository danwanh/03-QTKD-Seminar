# Review US-PAY-02 v2 — 07/11/2026

Kết luận: **Chờ xác nhận nghiệp vụ**; có một bất nhất kỹ thuật cần làm rõ và một điểm trình bày cần chỉnh. Không phát hiện phần sửa tự giải quyết mâu thuẫn đúng 500 triệu. Không sửa spec/sequence hoặc trả lời OQ thay nhóm.

## Nguồn và phạm vi

Đã đọc TA-SPEC §1–6, sys-pay-02(v2).md và diagrams/sequence-us-pay-02-v2.puml trong docs/analysis/payment-management/. Chỉ review US-PAY-02; không đánh giá bộ thiết kế/API/dữ liệu toàn module chưa được giao. TA-PDF chưa mở. Không dùng tài liệu ngoài phạm vi để giải OQ.

Review diễn ra trong cùng chat đã tham gia soạn bản trước; không phải review độc lập trong chat mới. Công cụ: Codex desktop, đọc tệp bằng dòng lệnh; phiên bản ứng dụng/model không được cung cấp. Prompt thực tế: “hãy xem phiên bản v2 tôi đã chỉnh sửa và review nó”. Không tạo subagent.

## Bao phủ

| Nội dung | Kết quả đối chiếu | Nguồn |
|---|---|---|
| Actor, Draft → PendingApproval, thông báo | Có B1–B7; quyền chỉ người lập vẫn phụ thuộc OQ-04, không xem là đã duyệt | TA-SPEC §2–3, §4.2 |
| Tổng âm, thiếu dịch vụ, chống trình trùng | Có B2/B3/B5, A2/A3/A4; danh mục bắt buộc còn OQ-01; phản hồi trùng cần làm rõ R01 | TA-SPEC §5 PAY-04 |
| Cấp duyệt, cấm tự duyệt | Có B4/A5; đúng 500 triệu còn OQ-02. Chặn trình khi người nhận trùng người lập là phương án G3/OQ-05, không phải nguyên văn PAY-07 | TA-SPEC §4.3, §5 PAY-06/07 |
| Audit | B5/A6 đề xuất ghi cùng giao dịch; chưa có bằng chứng chạy ứng dụng | TA-SPEC §6, gạch đầu dòng audit |
| Hiệu năng | Đúng khi tách ≤3 giây, <200 dòng cho chức năng lập bảng; không gán SLA trình duyệt | TA-SPEC §6, gạch đầu dòng lập bảng |
| Ranh giới | Không thêm trạng thái bảng hoặc CRUD module ngoài; không mở rộng sang duyệt/từ chối | TA-SPEC §1, §3, §4.2–4.3 |
| AC | Không có bộ AC riêng theo phạm vi người dùng đã bỏ; không coi đây là thiếu sót của lần sửa | Yêu cầu người dùng trước đó: bỏ US/AC |

## Nhận xét

| ID | Vị trí file/mục/dòng | Loại | Mức độ | Nhận xét và tác động | Đề xuất/cách kiểm chứng | Căn cứ trang/mục/US/PAY | OQ |
|---|---|---|---|---|---|---|---|
| R01 | sys-pay-02(v2).md dòng 14 B2, dòng 15 A2/A3; sequence group B2 và B5 | Nhất quán kỹ thuật | TB | A2 hứa yêu cầu trình trùng nhận kết quả đã trình. Sequence chỉ nhận diện sớm kết quả theo boardId, expectedVersion, requestKey; nếu thao tác lặp tạo requestKey mới và đến sau khi lần đầu đã hoàn tất, lookup có thể không khớp và rơi vào A3 vì không còn Draft, trả yêu cầu tải lại. Nhánh A2 ở B5 chỉ bao phủ yêu cầu đã đi đến giao dịch. Chưa rõ trường hợp trên thuộc A2 hay A3. Đây không phải kết luận rằng PAY-04 bị vi phạm: cả hai vẫn có thể chặn trình trùng. | Chốt cách phân biệt phát lại cùng khóa và thao tác trùng khác khóa trên cùng phiên bản; đồng bộ lời hứa phản hồi trong spec và sequence. Kiểm chứng hai lần gửi tuần tự khác khóa, hai lần đồng thời và bản Draft bị sửa giữa hai lần gửi. Không cần thêm trạng thái nghiệp vụ. | TA-SPEC §4.2; §5 PAY-04. Không có căn cứ trong đặc tả cho một mã/phản hồi bắt buộc; phần phản hồi là đề xuất kỹ thuật của v2. | OQ-06 |
| R02 | sys-pay-02(v2).md dòng 1–3, 10–15, 25; đối chiếu note/legend sequence | Phân loại và trạng thái tài liệu | Thấp | Bản sửa bỏ nhãn “GIẢ ĐỊNH – Cần xác nhận” cho G1–G4 và bỏ Design Pending Approval, trong khi sequence vẫn gọi các nhánh là mô phỏng/chưa phê duyệt. OQ vẫn được ghi mở, chưa có người trả lời nên không coi đây là việc tự chốt nghiệp vụ; tuy nhiên bảng UC khi đọc riêng dễ bị hiểu G1 là quyền chính thức. | Thêm một câu chung rõ G1–G4 là phương án giả định chưa xác nhận và khôi phục trạng thái Design Pending Approval; có thể giữ phần thân ngắn. Không cần lặp nhãn mọi ô. | TA-SPEC §2/§4.2 không quy định chỉ người lập được trình; §5 PAY-04 chưa có danh mục; quy tắc phân loại/không tự duyệt nghiệp vụ và trạng thái thiết kế trong AGENTS.md. | OQ-01/03/04/05/06 |

## Phần chưa kiểm chứng và bàn giao

Không chạy lại PlantUML hoặc mở ảnh SVG/PNG trong lần review này; chỉ đọc mã sequence. Bằng chứng kết xuất trong spec là lịch sử lần trước, không phải kết quả mới của reviewer. Không kiểm thử ứng dụng hoặc đo hiệu năng. Không có xác nhận nghiệp vụ mới; OQ-01..07 vẫn cần người phụ trách trả lời. Giữ ghi nhận OQ là đúng phạm vi, không báo lỗi chỉ vì OQ chưa được trả lời.

Nhóm đánh giá R01/R02 và ghi chấp nhận/từ chối/chờ theo quy trình; reviewer không tự phân loại nhận xét của mình thay nhóm. AI viết báo cáo này; chưa có ghi nhận nhóm sửa/phê duyệt báo cáo.

Bản spec được review, SHA-256: fee47d320161c6e9b3a0338ec2257a2073def504cdba7fdd2c8ed65e3011f877
