# Ngữ cảnh dùng chung cho các skill – Bảng thanh toán TA 1–2

Tài liệu tham chiếu cho mọi skill trong [skills/](../README.md). Không thay
[AGENTS.md](../../AGENTS.md); khi có khác biệt, AGENTS.md và TA-SPEC thắng.
Mọi dữ kiện dưới đây phải được kiểm tra lại trên file thực trước khi dùng.

## 1. Nguồn và cách dẫn

| Mã | File | Dùng để |
|---|---|---|
| TA-SPEC | [spec.md](../../docs/requirements/payment-management/spec.md) | Căn cứ nghiệp vụ duy nhất (cùng TA-PDF) |
| TA-PDF | [assignment-ta-1-2.pdf](../../docs/requirements/payment-management/assignment-ta-1-2.pdf) | Dẫn trang: §1–3 tr.1; §4–5 tr.2; §6 tr.3 |
| AS-IS | [src/Qtkd.Api/](../../src/Qtkd.Api) | Bằng chứng hiện trạng, không xác lập TO-BE |
| DATH, BA-DATH | `docs/requirements/QTKD_DATH.pdf`, `BA_QTKD_User_Stories.xlsx` | Chỉ bối cảnh; không dùng làm đáp án OQ |

Mẫu dẫn: `[ĐẶC TẢ] [TA-SPEC §4.3, US-PAY-03; TA-PDF tr.2]`.
Nhãn bắt buộc: `[ĐẶC TẢ]`, `[AC dẫn xuất]`, `[THAM KHẢO]`, `[ĐỀ XUẤT KỸ THUẬT]`,
`[GIẢ ĐỊNH – Cần xác nhận]`, `[QUYẾT ĐỊNH ĐÃ XÁC NHẬN]` (chỉ khi có người/ngày/tham chiếu).

## 2. Danh mục ID phải bao phủ

| ID | Nội dung rút gọn | Vị trí |
|---|---|---|
| US-PAY-01 | Lập bảng (NVKD), sinh dòng, tổng tiền, lưu Draft; sửa khi Draft | §4.1, tr.2 |
| US-PAY-02 | Trình duyệt (NVKD), kiểm tra PAY-04, → PendingApproval, thông báo người duyệt | §4.2, tr.2 |
| US-PAY-03 | Duyệt (→ Approved) / từ chối kèm lý do | §4.3, tr.2 |
| US-PAY-04 | KTT điều chỉnh bảng Approved khi có biên bản; ghi log | §4.4, tr.2 |
| US-PAY-05 | Hủy bảng Draft → Cancelled, không dùng lại | §4.5, tr.2 |
| PAY-01 | HĐ Active + bảng giá phù hợp; một bảng/HĐ/tháng | §5, tr.2 |
| PAY-02 | Sản lượng kỳ phải "Đã đối soát" | §5, tr.2 |
| PAY-03 | Thành tiền = sản lượng × đơn giá tại thời điểm tính | §5, tr.2 |
| PAY-04 | Chặn tổng âm/thiếu dòng bắt buộc; chống trình trùng | §5, tr.2 |
| PAY-05 | Approved không được sửa dưới bất kỳ hình thức nào | §5, tr.2 |
| PAY-06 | Trên 500 triệu → GĐKD; còn lại → KTT | §5, tr.2 |
| PAY-07 | Người lập không duyệt bảng mình lập | §5, tr.2 |
| PAY-08 | Từ chối phải có lý do; quay về Draft để sửa và trình lại | §5, tr.2 |
| NFR-PAY-01 | Audit mọi thay đổi trạng thái/điều chỉnh: ai, lúc nào, thay đổi gì | §6 gạch 1, tr.3 (mã nội bộ) |
| NFR-PAY-02 | Lập bảng ≤ 3 giây với HĐ có **dưới** 200 dòng | §6 gạch 2, tr.3 (mã nội bộ) |

Vai trò §2: NVKD, KTT, GĐKD. Trạng thái §3 (đúng chính tả, không thêm):
`Draft`, `PendingApproval`, `Approved`, `Rejected`, `Cancelled`.

Ánh xạ use case hệ thống: `SYS-PAY-0N` ↔ `US-PAY-0N` (file
`docs/analysis/payment-management/sys-pay-0N-<slug>.md`). Đã có:
[sys-pay-03-duyet-tu-choi.md](../../docs/analysis/payment-management/sys-pay-03-duyet-tu-choi.md)
– dùng làm mẫu định dạng.

## 3. Quy ước mã tự đặt

Mã tự đặt không phải mã trong đề; ghi rõ điều đó lần đầu xuất hiện.

| Loại | Mẫu | Nơi định nghĩa |
|---|---|---|
| AC dẫn xuất | `AC-US0N-kk` (vd. `AC-US03-02`) | Phần AC của `sys-pay-0N-*.md` hoặc `requirements-analysis.md` |
| OQ theo UC | `OQ-P0N-kk` (đang dùng ở sys-pay-03) | Phần 2 của `sys-pay-0N-*.md` |
| OQ dùng chung | Theo `open-questions.md` của BA (nếu đã có, giữ ánh xạ ID cũ) | `docs/analysis/payment-management/open-questions.md` |
| OQ mới do design | `OQ-D-kk` | Open Questions trong `01-requirements-summary.md` |
| Quyết định kỹ thuật | `DD-kk` | `07-design-decisions.md` |

Trước khi đặt mã mới: tìm mã đã có (`grep -rn "OQ-\|AC-US\|DD-" docs/`) để
tái sử dụng, không tạo trùng nghĩa.

## 4. Mâu thuẫn/thiếu đã biết – không tự chọn phía

| Vấn đề | Vị trí | OQ đã có (kiểm tra lại) |
|---|---|---|
| Đúng 500.000.000 đ ai duyệt | §4.3 "từ … trở lên" ↔ PAY-06 "trên" | OQ-P03-01 |
| Sau từ chối: Rejected hay Draft | §3 ↔ PAY-08 | OQ-P03-02 |
| Điều chỉnh Approved | §4.4 US-PAY-04 ↔ PAY-05 | OQ-P03-10 (theo dõi chung với SYS-PAY-04) |
| Kỳ tháng/quý ↔ duy nhất theo tháng | §2 ↔ PAY-01 | Chưa có ID tại 07/11/2026 |
| Dòng dịch vụ bắt buộc là gì | PAY-04 | Chưa có ID tại 07/11/2026 |
| Quyền hủy, phạm vi sửa Draft, làm tròn, VAT, lập lại sau hủy, kênh thông báo | §4.1, §4.5, PAY-03, §4.2 | Một phần ở OQ-P03-03, 08; còn lại chưa có ID |

Phần phụ thuộc ghi `Blocked by OQ-…`. Có thể vẽ/thiết kế các phương án nhưng
gắn `[GIẢ ĐỊNH – Cần xác nhận]` và không gọi là luồng cuối.

## 5. Ảnh chụp AS-IS (đọc file thực ngày 07/11/2026 – phải đọc lại)

- `src/Qtkd.Api/Qtkd.Api.csproj`: ASP.NET Core minimal API, `net8.0`, Nullable bật.
- `Program.cs`: endpoint `GET /`, `GET /api/contracts`, `GET /api/contracts/{id:int}`,
  `POST /api/contracts`, `POST /api/contracts/{id:int}/submit`; enum serialize dạng
  chuỗi (`JsonStringEnumConverter`); lỗi trả `ApiError(Code, Message)`, 404/400/409.
- `Services/ContractService.cs`: lưu trong bộ nhớ (`ConcurrentDictionary`), singleton,
  `lock (_gate)` khi Submit; mã lỗi `NOT_FOUND`, `INVALID_STATE`, `INVALID_CONTRACT`,
  `INVALID_DATE`; TODO Withdraw/authorization/audit.
- `Models/Contract.cs`: `ContractStatus { Draft, PendingApproval, RevisionRequested,
  Approved, Active }` – trạng thái của **hợp đồng**, không phải bảng thanh toán.
- Chưa có: module/entity bảng thanh toán, bảng giá, sản lượng, xác thực/phân quyền,
  audit log, logging cấu hình riêng, CSDL/migration, dự án kiểm thử.

Không suy ra rằng TO-BE phải dùng in-memory/lock; đó chỉ là hiện trạng demo.

## 6. Tên dùng chung giữa tài liệu, UML, API, dữ liệu

- Nguồn duy nhất của tên: mục **"Danh mục tên dùng chung"** trong
  `docs/design/payment-management/03-detailed-design.md` (class, enum, thao tác,
  sự kiện, endpoint, bảng/cột). Skill đầu tiên cần tên mà mục này chưa có thì
  ghi bảng **"Tên dùng tạm – cần đồng bộ vào 03"** trong đầu ra của mình.
- Tên trạng thái giữ nguyên 5 giá trị §3 ở mọi nơi (enum, state, cột, JSON).
- Một thao tác dùng cùng một động từ ở state event, sequence message, method,
  endpoint và audit action (vd. submit/approve/reject/cancel/adjust).
- Khác biệt tên giữa các file là lỗi phải sửa trước khi bàn giao.

## 7. Kiểm chứng PlantUML

Máy hiện có Java và Graphviz; chưa thấy `plantuml` trên PATH (07/11/2026).
Có `plantuml.jar` thì chạy, ghi lệnh và kết quả:

```sh
java -jar plantuml.jar -checkonly docs/design/payment-management/diagrams/*.puml
java -jar plantuml.jar -tsvg docs/design/payment-management/diagrams/*.puml
```

Không chạy được thì ghi đúng câu `Chưa kiểm tra kết xuất sơ đồ` cạnh danh mục sơ đồ.
