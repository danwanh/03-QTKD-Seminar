# -*- coding: utf-8 -*-
"""Sinh file Excel phân tích US từ QTKD_DATH.pdf. Không bổ sung nghiệp vụ."""
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from pathlib import Path

OUT = Path(__file__).with_name("BA_QTKD_User_Stories.xlsx")
SRC = "QTKD_DATH.pdf"

wb = Workbook()

thin = Border(
    left=Side(style="thin", color="D0D5DD"),
    right=Side(style="thin", color="D0D5DD"),
    top=Side(style="thin", color="D0D5DD"),
    bottom=Side(style="thin", color="D0D5DD"),
)
fill_h = PatternFill("solid", fgColor="1F4E79")
fill_note = PatternFill("solid", fgColor="FFF4CC")
fill_alt = PatternFill("solid", fgColor="F2F4F7")
font_h = Font(bold=True, color="FFFFFF", name="Calibri", size=11)
font_n = Font(name="Calibri", size=10)
wrap = Alignment(wrap_text=True, vertical="top")


def style_header(ws, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(1, c)
        cell.fill = fill_h
        cell.font = font_h
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = thin
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    ws.row_dimensions[1].height = 28


def dump(ws, headers, rows, widths):
    ws.append(headers)
    for i, row in enumerate(rows):
        ws.append(list(row))
        fill = fill_alt if i % 2 else None
        for c in range(1, len(headers) + 1):
            cell = ws.cell(i + 2, c)
            cell.font = font_n
            cell.alignment = wrap
            cell.border = thin
            if fill:
                cell.fill = fill
            if headers[c - 1] == "Can_xac_nhan" and cell.value and str(cell.value) != "Khong":
                cell.fill = fill_note
        ws.row_dimensions[i + 2].height = 90
    style_header(ws, len(headers))
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


# --- 00 Ghi chu ---
ws = wb.active
ws.title = "00_Ghi_chu"
notes = [
    ["Muc", "Noi dung"],
    ["Nguon bat buoc theo ba.md", "Chi doc docs/requirements/QTKD_DATH.pdf (6 trang)."],
    ["Ghi chu workspace", "Rule qtkd-context yeu cau docs/business-rules.md; tai thoi diem phan tich file nay KHONG CON trong repo. Khong suy dien rule tu ban mau cu."],
    ["Phuong phap", "DATH khong danh so User Story. US_ID duoi day la cau truc BA map 1-1 tu chuc nang muc 4, vai tro muc 2, quy trinh muc 3, rule muc 5. Khong tu them hanh vi ngoai tai lieu."],
    ["Phan biet", "Muc 5.5 va muc 6 la rang buoc/de xuat KY THUAT, khong phai business rule moi. Ghi o sheet 05."],
    ["Acceptance criteria", "DATH khong viet AC dang Given/When/Then. Cot AC chi restatement dieu kien/ket qua DA NOI trong muc 4 va muc 5. Thieu thi ghi Can xac nhan."],
    ["Luong", "Main/alternative chi ghi buoc co trong tai lieu. Buoc UI, dang nhap, API, ma HTTP: Can xac nhan neu DATH khong noi."],
    ["Trang PDF", "Trang 1 bia; trang 2 muc 1-4.2; trang 3 muc 4.3-4.10; trang 4 muc 5.1-5.2; trang 5 muc 5.3-5.5; trang 6 het 5.5 + muc 6."],
]
for r in notes:
    ws.append(r)
style_header(ws, 2)
ws.column_dimensions["A"].width = 28
ws.column_dimensions["B"].width = 110
for r in range(2, 9):
    ws.cell(r, 1).font = Font(bold=True, name="Calibri", size=10)
    ws.cell(r, 1).alignment = wrap
    ws.cell(r, 2).alignment = wrap
    ws.cell(r, 1).border = thin
    ws.cell(r, 2).border = thin
    ws.row_dimensions[r].height = 48

# --- 01 Actor ---
ws = wb.create_sheet("01_Actor")
dump(
    ws,
    ["Actor", "Phong_ban_DATH", "Vai_tro_nghiep_vu", "Can_cu"],
    [
        ["Nhan vien Kinh doanh", "Kinh doanh", "Quan ly khach hang, tao hop dong, de xuat bang gia, theo doi tinh trang ky ket.", "QTKD_DATH.pdf, muc 2, trang 2"],
        ["Nhan vien Khai thac", "Khai thac", "Ghi nhan san luong thuc te, kiem tra du lieu van hanh, doi soat san luong.", "QTKD_DATH.pdf, muc 2, trang 2"],
        ["Nhan vien Ke toan", "Ke toan", "Kiem tra ho so thanh toan, lap/kiem tra bang thanh toan, theo doi cong no.", "QTKD_DATH.pdf, muc 2, trang 2"],
        ["Nhan vien Phap che", "Phap che", "Ra soat dieu khoan hop dong, kiem tra phu luc, gop y truoc khi trinh ky.", "QTKD_DATH.pdf, muc 2, trang 2"],
        ["Ban Giam doc", "Ban Giam doc", "Phe duyet hop dong, bang gia, bang thanh toan va cac ho so quan trong.", "QTKD_DATH.pdf, muc 2, trang 2"],
        ["Quan tri he thong", "Quan tri he thong", "Quan ly nguoi dung, phan quyen, cau hinh workflow, cau hinh loai ho so.", "QTKD_DATH.pdf, muc 2, trang 2"],
        ["Nguoi dung duoc giao buoc hien tai (assignee)", "Tuy quy trinh", "Chi assignee buoc hien tai duoc approve/reject/request revision. Kiem tra role la chua du.", "QTKD_DATH.pdf, APR-01 va 5.5 Phan quyen theo ngu canh, trang 5-6"],
        ["He thong / dich vu ky dien tu / Notification Service", "Ky thuat", "Xu ly bat dong bo, callback/webhook, thong bao event. Khong phai actor nghiep vu phong ban.", "QTKD_DATH.pdf, muc 4.8-4.9, APR-06, APR-07, trang 3 va 5"],
    ],
    [38, 22, 70, 45],
)

# --- stories ---
# AC/precondition/flows: only from document
stories = [
    dict(
        us_id="US-CUS-01",
        ten="Tao khach hang",
        story="Là nhân viên Kinh doanh, tôi muốn tạo mới khách hàng (mã, tên, MST, địa chỉ, người đại diện, liên hệ, trạng thái) để quản lý vòng đời hồ sơ theo khách hàng.",
        muc="4.1",
        trang="2",
        actor="Nhan vien Kinh doanh",
        pre="Cần xác nhận: tài liệu không nêu điều kiện tiên quyết (đăng nhập, mã khách hàng unique, MST hợp lệ).",
        main="1) Actor tạo mới khách hàng.\n2) Hệ thống lưu mã, tên, MST, địa chỉ, người đại diện, thông tin liên hệ, trạng thái.",
        alt="Cần xác nhận: DATH không mô tả luồng lỗi (trùng mã, thiếu trường).",
        rules="Khong co ma rule rieng cho khach hang trong muc 5.",
        ac="AC: He thong luu duoc cac thuoc tinh liet ke o muc 4.1.\nCon lai: Cần xác nhận (khong co AC chi tiet).",
        cxn="Trạng thái khách hàng có những giá trị nào? Tạo mới mặc định trạng thái gì? Ai ngoài Kinh doanh được tạo?",
    ),
    dict(
        us_id="US-CUS-02",
        ten="Cap nhat khach hang",
        story="Là nhân viên Kinh doanh, tôi muốn cập nhật thông tin khách hàng đã có.",
        muc="4.1",
        trang="2",
        actor="Nhan vien Kinh doanh",
        pre="Khách hàng đã tồn tại (suy ra từ 'cập nhật'). Cần xác nhận quyền và trường được sửa.",
        main="Actor cập nhật khách hàng; hệ thống lưu thay đổi các thuộc tính mục 4.1.",
        alt="Cần xác nhận.",
        rules="Khong co ma rule rieng. Neu cap nhat la thay doi quan trong: Cần xác nhận co ghi audit 4.10 hay khong.",
        ac="AC: Cap nhat duoc khach hang da ton tai. Chi tiet validation: Cần xác nhận.",
        cxn="Có hạn chế sửa khi khách hàng đang gắn hợp đồng Active không? DATH không nói.",
    ),
    dict(
        us_id="US-CUS-03",
        ten="Tam ngung khach hang",
        story="Là nhân viên Kinh doanh, tôi muốn tạm ngưng khách hàng.",
        muc="4.1",
        trang="2",
        actor="Nhan vien Kinh doanh",
        pre="Khách hàng đã tồn tại. Cần xác nhận điều kiện được tạm ngưng.",
        main="Actor tạm ngưng khách hàng; trạng thái khách hàng thay đổi (mục 4.1 có trường trạng thái).",
        alt="Cần xác nhận: hệ quả với hợp đồng/bảng giá đang hiệu lực không được mô tả.",
        rules="Khong co ma rule.",
        ac="AC: Thuc hien duoc hanh dong tam ngung. Hieu ung len hop dong: Cần xác nhận.",
        cxn="Tạm ngưng có chặn tạo hợp đồng/bảng giá/thanh toán mới không? Có hoàn tác không?",
    ),
    dict(
        us_id="US-CUS-04",
        ten="Tra cuu ho so theo khach hang",
        story="Là người dùng nghiệp vụ, tôi muốn tra cứu hợp đồng, bảng giá, bảng thanh toán đã phát sinh theo khách hàng.",
        muc="4.1",
        trang="2",
        actor="Cần xác nhận actor: 4.1 khong chi dinh phong ban; muc 2 giao Kinh doanh quan ly khach hang.",
        pre="Khách hàng đã tồn tại; có hoặc không có hồ sơ phát sinh.",
        main="Actor chọn khách hàng; hệ thống cho phép tra cứu HĐ, bảng giá, bảng thanh toán gắn khách hàng đó.",
        alt="Cần xác nhận hành vi khi chưa có hồ sơ.",
        rules="Khong co ma rule.",
        ac="AC: Tra cuu duoc cac hop dong, bang gia, bang thanh toan da phat sinh theo khach hang (muc 4.1).",
        cxn="Pháp chế/Kế toán/BGD có được tra cứu không? Phạm vi dữ liệu theo quyền?",
    ),
    dict(
        us_id="US-CTR-01",
        ten="Tao hop dong",
        story="Là nhân viên Kinh doanh, tôi muốn tạo hợp đồng với khách hàng, thời gian hiệu lực, giá trị, điều khoản thanh toán, điều khoản dịch vụ và tệp đính kèm.",
        muc="3 buoc 1; 4.2",
        trang="2",
        actor="Nhan vien Kinh doanh (muc 2, muc 3.1)",
        pre="Cần xác nhận: khách hàng phải tồn tại trước khi tạo HĐ? Muc 3.1 noi tao thong tin KH va ho so HĐ, khong bat buoc thu tu he thong.",
        main="1) Kinh doanh tao ho so hop dong.\n2) Thong tin gom: khach hang, thoi gian hieu luc, gia tri, dieu khoan thanh toan, dieu khoan dich vu, tep dinh kem.",
        alt="Cần xác nhận validation khi thieu truong.",
        rules="CTR-01 (sau khi tao, sua chi o Draft/Revision Requested). Trang thai khoi tao: Cần xác nhận (DATH dinh huong Draft o CTR-01).",
        ac="AC: Tao duoc hop dong voi cac nhom thong tin liet ke muc 4.2.",
        cxn="Trạng thái tạo mới có phải Draft không? Giá trị hợp đồng bắt buộc? Định dạng tệp?",
    ),
    dict(
        us_id="US-CTR-02",
        ten="Chinh sua hop dong",
        story="Là nhân viên Kinh doanh, tôi muốn chỉnh sửa hợp đồng khi còn ở trạng thái được phép.",
        muc="4.2; 5.1 CTR-01, CTR-07",
        trang="2 va 4",
        actor="Nhan vien Kinh doanh (Cần xác nhận neu Phap che cung sua sau request revision)",
        pre="Hop dong ton tai va o Draft hoac Revision Requested (CTR-01).",
        main="Actor chinh sua hop dong o trang thai cho phep; he thong luu thay doi.",
        alt="A1. Khong o Draft/Revision Requested -> khong cho sua (CTR-01).\nA2. Active/Approved va thay doi dieu khoan quan trong -> phai tao phu luc, khong sua truc tiep (CTR-07).",
        rules="CTR-01, CTR-07. CTR-04: Rejected khong duoc tu dong sua va submit lai.",
        ac="AC1: Sua duoc khi Draft hoac Revision Requested.\nAC2: Khong sua duoc ngoai cac trang thai do (CTR-01).\nAC3: Thay doi dieu khoan quan trong khi Approved/Active phai qua phu luc (CTR-07).\n'Dieu khoan quan trong' : Cần xác nhận.",
        cxn="Danh muc dieu khoan quan trong? Revision Requested do ai chuyen? Rejected xu ly bang ban chinh sua hay ve Revision (CTR-04 de nhom thiet ke)?",
    ),
    dict(
        us_id="US-CTR-03",
        ten="Gui hop dong trinh duyet",
        story="Là nhân viên Kinh doanh, tôi muốn gửi hợp đồng trình duyệt để hồ sơ đi qua luồng rà soát/phê duyệt, không chuyển thẳng Approved.",
        muc="3 buoc 2; 4.2; 4.7; 5.1 CTR-02 CTR-03; 5.5 Double submit",
        trang="2, 3, 4, 5",
        actor="Nhan vien Kinh doanh. Luong ra soat: Kinh doanh, Phap che, Ban Giam doc (muc 3.2).",
        pre="Hop dong da ton tai. CTR-02: khach hang hop le, thoi gian hieu luc hop le, it nhat mot tep/hang muc noi dung bat buoc. Khong chuyen Draft->Approved (CTR-03).",
        main="1) Actor gui hop dong trinh duyet.\n2) He thong kiem tra dieu kien CTR-02.\n3) Khoi tao quy trinh phe duyet (khong hard-code if/else don gian — muc 4.7, day la yeu cau thiet ke).\n4) Theo doi nguoi dang xu ly va lich su xu ly (4.2, 4.7, 4.10).",
        alt="A1. Khong du CTR-02 -> khong duoc Submit.\nA2. Khong duoc nhay Draft thanh Approved (CTR-03).\nA3. Bam Submit nhieu lan khong tao nhieu workflow instance (muc 5.5 Double submit).\nA4. Rejected: khong tu dong sua+submit; can ban chinh sua hoac ve Revision (CTR-04, Cần xác nhận cach chon).",
        rules="CTR-02, CTR-03, CTR-04; APR-05 (ket thuc duyet -> Approved, ngoai US nay). Muc 5.5 Double submit = rang buoc ky thuat gan rule.",
        ac="AC1: Submit chi khi du CTR-02.\nAC2: Sau submit phai qua quy trinh phe duyet, khong Approved ngay (CTR-03).\nAC3: Submit lap khong tao nhieu workflow instance (5.5).\nTrang thai sau submit: Cần xác nhận ten trang thai (DATH khong dat ten Pending Approval).",
        cxn="Ten trang thai sau Submit? Ai duoc bam Submit (chi nguoi tao hay moi Kinh doanh)? Danh muc tep/hang muc bat buoc? Idempotency-Key la de xuat ky thuat, chua phai rule nghiep vu.",
    ),
    dict(
        us_id="US-CTR-04",
        ten="Theo doi xu ly hop dong",
        story="Là nhân viên Kinh doanh (và bên liên quan quy trình), tôi muốn theo dõi người đang xử lý và lịch sử xử lý hợp đồng.",
        muc="4.2; 4.7; 4.10",
        trang="2-3",
        actor="Kinh doanh (4.2). Muc 4.7: nguoi dung theo doi tien do — Cần xác nhận pham vi actor.",
        pre="Hop dong da ton tai.",
        main="He thong hien thi nguoi dang xu ly, cac buoc da hoan thanh va con lai (4.7); lich su ai/thoi diem/hanh dong/trang thai truoc-sau/ghi chu (4.10).",
        alt="Cần xác nhận khi chua gui duyet (chua co buoc).",
        rules="Khong ma rieng. Audit khong phu thuoc du lieu hien thi hien tai (4.10).",
        ac="AC1: Xem duoc nguoi dang xu ly va tien do buoc (4.7).\nAC2: Tra cuu lich su theo hop dong (4.10).",
        cxn="Pháp chế/BGD xem cùng màn hình? Deadline bước có bắt buộc hiển thị không? DATH không nói hạn xử lý.",
    ),
    dict(
        us_id="US-CTR-05",
        ten="Gia han hop dong",
        story="Là nhân viên Kinh doanh, tôi muốn gia hạn hợp đồng.",
        muc="4.2",
        trang="2",
        actor="Nhan vien Kinh doanh",
        pre="Cần xác nhận: chi gia han khi Active/Approved? CTR-07 co the yeu cau phu luc neu la thay doi dieu khoan quan trong.",
        main="Actor thuc hien gia han hop dong (muc 4.2 liet ke hanh dong, khong mo ta buoc).",
        alt="Cần xác nhận: gia han co phai tao phu luc va phe duyet lai.",
        rules="CTR-07 neu gia han duoc xem la thay doi dieu khoan quan trong — Cần xác nhận phan loai.\nCTR-05: Approved chi Active khi den ngay hieu luc (lien quan ngay, khong mo ta gia han).",
        ac="AC: Thuc hien duoc hanh dong gia han (muc 4.2). Chi tiet ket qua: Cần xác nhận.",
        cxn="Gia hạn = phụ lục hay sửa ngày hiệu lực? Có qua phê duyệt không? Ảnh hưởng bảng giá đang hiệu lực?",
    ),
    dict(
        us_id="US-CTR-06",
        ten="Huy hop dong",
        story="Là nhân viên Kinh doanh, tôi muốn hủy hợp đồng. Hợp đồng Active không được xóa.",
        muc="4.2; CTR-06",
        trang="2 va 4",
        actor="Cần xác nhận: muc 4.2 khong chi actor; muc 2 Kinh doanh quan ly hop dong. Quyen huy Active: Cần xác nhận.",
        pre="Hop dong da ton tai.",
        main="Actor huy hop dong; he thong chuyen trang thai theo quy tac nghiep vu (Cancelled — CTR-06 dung chu Cancelled/Expired).",
        alt="A1. Active khong duoc xoa; phai chuyen Cancelled hoac Expired (CTR-06).\nA2. Expired: Cần xác nhận co phai hanh dong nguoi dung hay tu dong het han.",
        rules="CTR-06.",
        ac="AC1: Khong xoa hop dong Active.\nAC2: Khong su dung nua phai chuyen Cancelled hoac Expired (CTR-06).\nDieu kien duoc bam Huy: Cần xác nhận.",
        cxn="Ai được hủy? Hủy Draft khác hủy Active? Expired tự động theo ngày kết thúc?",
    ),
    dict(
        us_id="US-ADD-01",
        ten="Tao phu luc hop dong",
        story="Là nhân viên Kinh doanh, tôi muốn tạo phụ lục gắn hợp đồng đã tồn tại để thay đổi đơn giá, thời hạn, điều khoản thanh toán hoặc bổ sung dịch vụ.",
        muc="4.2; 4.3; CTR-07",
        trang="2-4",
        actor="Kinh doanh (tao). Phap che kiem tra phu luc (muc 2).",
        pre="Hop dong da ton tai (4.3). Neu HĐ Active/Approved va thay doi dieu khoan quan trong: bat buoc phu luc (CTR-07).",
        main="1) Tao phu luc gan hop dong hien co.\n2) Noi dung co the: don gia, thoi han hieu luc, dieu khoan thanh toan, bo sung dich vu.",
        alt="Cần xác nhận neu hop dong chua duyet / Draft.",
        rules="CTR-07.",
        ac="AC1: Phu luc phai gan hop dong da ton tai.\nAC2: Approved/Active khong sua truc tiep dieu khoan quan trong ma tao phu luc (CTR-07).",
        cxn="Phụ lục khi HĐ còn Draft có được không? Trường bắt buộc của phụ lục?",
    ),
    dict(
        us_id="US-ADD-02",
        ten="Phe duyet phu luc",
        story="Là bên trong luồng phê duyệt, tôi muốn phụ lục đi qua luồng phê duyệt tương tự hoặc khác hợp đồng chính tùy cấu hình.",
        muc="4.3; 4.7; muc 2 Phap che/BGD",
        trang="3",
        actor="Cau hinh workflow (Quan tri). Nguoi duyet theo assignee (APR-01).",
        pre="Phu luc da tao. Quy trinh theo loai ho so da duoc cau hinh (4.7, 4.3).",
        main="Phu luc di luong phe duyet (tuong tu hoac khac HĐ chinh tuy cau hinh).",
        alt="Tu choi / yeu cau chinh sua / reject theo APR-01..APR-04.",
        rules="APR-01 den APR-05 (ap dung ho so noi chung). 4.3: luong tuong tu hoac khac tuy cau hinh.",
        ac="AC: Phu luc khong co hieu luc truoc khi qua luong phe duyet da cau hinh (suy ra tu 4.3 + CTR-03 tinh than). Chi tiet: Cần xác nhận.",
        cxn="Mặc định luồng phụ lục = luồng HĐ chính hay bắt buộc cấu hình riêng?",
    ),
    dict(
        us_id="US-ADD-03",
        ten="Ap dung phu luc khi co hieu luc",
        story="Sau khi phụ lục có hiệu lực, các nghiệp vụ phát sinh sau thời điểm hiệu lực phải dùng thông tin mới.",
        muc="4.3",
        trang="3",
        actor="He thong ap dung. Nguoi dung nghiep vu (Khai thac/Ke toan) thao tac phat sinh sau ngay hieu luc.",
        pre="Phu luc da co hieu luc (4.3). Cần xác nhận dieu kien 'co hieu luc' (da duyet? den ngay?).",
        main="Nghiep vu phat sinh SAU thoi diem hieu luc su dung thong tin moi cua phu luc.",
        alt="Cần xác nhận nghiep vu phat sinh TRUOC ngay hieu luc van dung ban cu.",
        rules="Khong ma rieng ngoai 4.3. Lien he CTR-05 (ngay hieu luc) — Cần xác nhận co ap dung giong HĐ.",
        ac="AC: Sau hieu luc, nghiep vu moi dung thong tin phu luc (4.3).",
        cxn="Phụ lục Effective ngay khi Approved hay chờ ngày hiệu lực? Ảnh hưởng bảng giá/sản lượng/thanh toán kỳ đang mở?",
    ),
    dict(
        us_id="US-PRC-01",
        ten="Tao bang gia",
        story="Là nhân viên Kinh doanh (hoặc bộ phận phụ trách), tôi muốn tạo bảng giá theo khách hàng, hợp đồng, nhóm/loại dịch vụ, có thời gian hiệu lực từ-đến.",
        muc="3 buoc 3-4; 4.4; PRC-01 PRC-02",
        trang="2-4",
        actor="Kinh doanh hoac bo phan phu trach (muc 3.3).",
        pre="Muc 3.3: sau khi hop dong duoc duyet. PRC-01: phai gan KH, HĐ, nhom DV hoac pham vi ro rang.",
        main="1) Tao bang gia theo KH/HĐ/nhom DV/loai DV.\n2) Khai bao hieu luc tu ngay den ngay.",
        alt="A1. Thieu pham vi ap dung -> vi pham PRC-01.\nA2. Ngay bat dau > ngay ket thuc -> vi pham PRC-02.",
        rules="PRC-01, PRC-02. Muc 3.3 noi tao sau khi HĐ duyet — Cần xác nhận co bat buoc o he thong hay chi quy trinh nghiep vu.",
        ac="AC1: Bang gia co pham vi ap dung ro (PRC-01).\nAC2: Co thoi gian hieu luc va start <= end (PRC-02).",
        cxn="Có tạo bảng giá khi HĐ còn Draft không? Bắt buộc gắn đúng một HĐ hay được theo nhóm KH?",
    ),
    dict(
        us_id="US-PRC-02",
        ten="Quan ly phien ban bang gia",
        story="Tôi muốn quản lý nhiều phiên bản bảng giá và lịch sử thay đổi; version mới làm version cũ Superseded hoặc hết hiệu lực theo ngày; không chồng Effective cùng đối tượng cùng loại dịch vụ.",
        muc="4.4; PRC-03 PRC-04 PRC-05",
        trang="3-4",
        actor="Cần xác nhận: Kinh doanh tao version; ai duoc sua.",
        pre="Bang gia da co. PRC-05: neu da dung de sinh bang thanh toan thi khong sua truc tiep.",
        main="Tao version moi; version cu Superseded hoac het hieu luc theo ngay (PRC-04); luu lich su (4.4, 4.10).",
        alt="A1. Hai bang gia Effective chong thoi gian cung doi tuong cung loai DV -> khong cho phep (PRC-03, 4.4).\nA2. Da dung cho thanh toan -> phai tao version moi (PRC-05).",
        rules="PRC-03, PRC-04, PRC-05.",
        ac="AC1: Khong hai Effective chong nhau cung doi tuong+loai DV (PRC-03).\nAC2: Version moi ke thua xu ly version cu theo PRC-04.\nAC3: Khong sua truc tiep bang gia da dung cho thanh toan (PRC-05).",
        cxn="'Cùng loại dịch vụ' và 'cùng đối tượng' định nghĩa thế nào? Overlap 1 ngày biên có tính chồng?",
    ),
    dict(
        us_id="US-PRC-03",
        ten="Phe duyet bang gia / dua vao hieu luc",
        story="Bảng giá được phê duyệt và có hiệu lực theo thời gian. Ban Giám đốc phê duyệt bảng giá.",
        muc="3 buoc 4; muc 2 BGD; PRC-03 Effective; PRC-06 Rejected",
        trang="2, 4",
        actor="Ban Giam doc phe duyet. Assignee buoc hien tai (APR-01).",
        pre="Bang gia da duoc gui vao quy trinh (4.7). Cần xác nhận actor Submit bang gia.",
        main="Bang gia qua phe duyet; co hieu luc theo thoi gian da khai bao.",
        alt="A1. Rejected: co the chinh sua va submit lai NEU nhom thiet ke cho phep (PRC-06) — Cần xác nhận.\nA2. Cac nhánh APR-01..APR-04.",
        rules="PRC-06 (co dieu kien 'neu nhom thiet ke cho phep'). APR-01..APR-05.",
        ac="AC: Bang gia hieu luc theo thoi gian sau phe duyet (muc 3.4). PRC-06 chua chot.",
        cxn="PRC-06 có cho phép resubmit sau Reject không? Effective ngay Approved hay chờ start date?",
    ),
    dict(
        us_id="US-VOL-01",
        ten="Ghi nhan san luong thuc te",
        story="Là nhân viên Khai thác, tôi muốn ghi nhận sản lượng thực tế theo kỳ (container, tấn, chuyến, ngày lưu kho) làm đầu vào bảng thanh toán.",
        muc="3 buoc 5; 4.5; muc 2",
        trang="2-3",
        actor="Nhan vien Khai thac",
        pre="Cần xác nhận: hop dong Active? bang gia hieu luc? khoa ky chua mo?",
        main="Khai thac ghi nhan san luong thuc te theo ky voi cac chi tieu: so container, so tan, so chuyen, so ngay luu kho.",
        alt="Cần xác nhận khi ky da khoa.",
        rules="Khong ma VOL. PAY-02 lien quan chat luong du lieu dau vao thanh toan.",
        ac="AC: Ghi nhan duoc cac loai san luong liet ke (4.5). Du lieu la dau vao lap bang thanh toan.",
        cxn="Bắt buộc gắn hợp đồng/dịch vụ nào? Đơn vị đo cố định? Ai xác nhận/đối soát (muc 2: Khai thác đối soát)?",
    ),
    dict(
        us_id="US-VOL-02",
        ten="Dieu chinh san luong truoc khoa ky",
        story="Là nhân viên Khai thác, tôi muốn điều chỉnh dữ liệu sản lượng trước khi khóa kỳ.",
        muc="4.5",
        trang="3",
        actor="Khai thac. Cần xác nhận actor doi soat.",
        pre="Ky chua khoa.",
        main="Dieu chinh du lieu san luong truoc khoa ky.",
        alt="Sau khoa ky: khong chinh sua neu khong co quyen dac biet (4.5) — xem US-VOL-03.",
        rules="Khong ma. 4.5 mo ta hanh vi.",
        ac="AC: Dieu chinh duoc truoc khoa ky.",
        cxn="Có phê duyệt điều chỉnh không? Có audit bắt buộc không (4.10 áp dụng chung)?",
    ),
    dict(
        us_id="US-VOL-03",
        ten="Khoa ky san luong / sua sau khoa ky",
        story="Sau khi khóa kỳ, dữ liệu không được chỉnh sửa nếu không có quyền đặc biệt.",
        muc="4.5",
        trang="3",
        actor="Cần xác nhận ai khoa ky. Quyen dac biet: Cần xác nhận vai tro.",
        pre="Du lieu san luong cua ky da ghi nhan.",
        main="Khoa ky. Sau do khong sua neu khong co quyen dac biet.",
        alt="Nguoi co quyen dac biet van sua duoc (4.5). Chi tiet luong: Cần xác nhận.",
        rules="Khong ma. PAY-02: san luong dung tinh phi phai thuoc ky va da xac nhan/doi soat theo quy tac nhom thiet ke.",
        ac="AC: Sau khoa ky, user thuong khong sua duoc (4.5).",
        cxn="Ai khóa kỳ? 'Quyền đặc biệt' là ai? PAY-02 'xác nhận/đối soát' khác khóa kỳ thế nào?",
    ),
    dict(
        us_id="US-PAY-01",
        ten="Lap bang thanh toan",
        story="Là nhân viên Kế toán, tôi muốn lập bảng thanh toán dựa trên hợp đồng còn hiệu lực, bảng giá phù hợp tại kỳ, và sản lượng thực tế; lưu đơn giá tại thời điểm tính.",
        muc="3 buoc 6; 4.6; PAY-01 PAY-02 PAY-03",
        trang="2, 3, 5",
        actor="Ke toan",
        pre="PAY-01: HĐ con hieu luc va co bang gia phu hop tai ky tinh phi.\nPAY-02: San luong thuoc ky va da xac nhan/doi soat (quy tac nhom thiet ke — Cần xác nhận).",
        main="Lap bang gom: danh sach dich vu, don gia, san luong tinh phi, thanh tien, thue, tong tien (4.6). Luu don gia tai thoi diem tinh (PAY-03; 5.5 Du lieu lich su).",
        alt="A1. HĐ khong hieu luc hoac thieu bang gia phu hop -> khong lap (PAY-01).\nA2. San luong chua du dieu kien PAY-02 -> Cần xác nhận chan hay canh bao.",
        rules="PAY-01, PAY-02, PAY-03.",
        ac="AC1: Chi lap khi PAY-01 thoa.\nAC2: Bang co du cac cot muc 4.6.\nAC3: Don gia luu tai thoi diem tinh, khong doi theo bang gia version moi (PAY-03).",
        cxn="PAY-02 chi tiết xác nhận/đối soát? Thuế suất lấy từ đâu? Một kỳ một bảng hay nhiều bảng/HĐ?",
    ),
    dict(
        us_id="US-PAY-02",
        ten="Doi chieu / chinh sua bang thanh toan truoc duyet",
        story="Là nhân viên Kế toán, tôi muốn đối chiếu/chỉnh sửa có kiểm soát trước khi trình duyệt.",
        muc="4.6; PAY-04 PAY-05",
        trang="3, 5",
        actor="Ke toan",
        pre="Bang thanh toan chua Approved/Signed (PAY-05 cam sua sau cac trang thai do).",
        main="Doi chieu/chinh sua co kiem soat truoc khi trinh duyet.",
        alt="Sau Approved hoac Signed: khong sua truc tiep; phai ho so dieu chinh hoac huy theo quy trinh (PAY-05) — US-PAY-04.",
        rules="PAY-04 (lien quan submit), PAY-05.",
        ac="AC: Truoc duyet, cho phep doi chieu/chinh sua co kiem soat (4.6). 'Kiem soat' chi tiet: Cần xác nhận.",
        cxn="'Có kiểm soát' nghĩa là gì (maker-checker, log, lý do)?",
    ),
    dict(
        us_id="US-PAY-03",
        ten="Trinh duyet bang thanh toan",
        story="Là nhân viên Kế toán, tôi muốn trình phê duyệt bảng thanh toán. Ban Giám đốc phê duyệt các hồ sơ quan trọng.",
        muc="3 buoc 7; 4.6; 4.7; PAY-04; muc 2 BGD",
        trang="2, 3, 5",
        actor="Ke toan gui. BGD / assignee duyet (APR-01).",
        pre="PAY-04: khong submit neu tong tien am hoac thieu dong dich vu bat buoc.",
        main="Gui bang thanh toan vao quy trinh phe duyet (4.7). Sau duyet, co the gui ky dien tu (PAY-06, US-ESN-01).",
        alt="A1. Tong tien am hoac thieu dong bat buoc -> khong submit (PAY-04).\nA2. Double submit khong tao nhieu workflow (5.5).",
        rules="PAY-04; APR-01..APR-05; 5.5 Double submit.",
        ac="AC1: Chan submit khi tong tien am hoac thieu dong bat buoc (PAY-04).\nAC2: Submit lap khong nhan doi workflow (5.5).",
        cxn="Dòng dịch vụ bắt buộc là gì? Tổng tiền = 0 có được submit không (chỉ cấm âm)?",
    ),
    dict(
        us_id="US-PAY-04",
        ten="Ho so dieu chinh / huy bang thanh toan sau duyet hoac ky",
        story="Sau khi bảng thanh toán được duyệt và ký, không được sửa trực tiếp mà phải tạo hồ sơ điều chỉnh hoặc hủy theo quy trình.",
        muc="4.6; PAY-05",
        trang="3, 5",
        actor="Cần xác nhận: Ke toan lap dieu chinh? Ai duyet huy?",
        pre="Bang o Approved hoac Signed (PAY-05).",
        main="Tao ho so dieu chinh hoac huy theo quy trinh; khong sua truc tiep bang goc.",
        alt="Cần xác nhận luong huy vs dieu chinh.",
        rules="PAY-05.",
        ac="AC: Khong sua truc tiep sau Approved/Signed; phai dieu chinh hoac huy (PAY-05, 4.6).",
        cxn="Hồ sơ điều chỉnh có phải loại hồ sơ riêng và workflow riêng không? Signed khác Approved ở chỗ e-sign?",
    ),
    dict(
        us_id="US-APR-01",
        ten="Cau hinh quy trinh phe duyet theo loai ho so",
        story="Là quản trị hệ thống, tôi muốn cấu hình workflow và loại hồ sơ vì mỗi loại hồ sơ có thể có quy trình khác nhau và không hard-code if/else đơn giản.",
        muc="2 Quan tri; 4.7; 4.3 phu luc",
        trang="2-3",
        actor="Quan tri he thong",
        pre="Cần xác nhận danh muc loai ho so toi thieu (HĐ, phu luc, bang gia, thanh toan).",
        main="Cau hinh workflow theo loai ho so.",
        alt="Cần xác nhận thay doi workflow khi dang co ho so dang chay.",
        rules="Khong ma. Yeu cau 4.7: khong hard-code if/else don gian — day la rang buoc THIET KE.",
        ac="AC: Moi loai ho so co the co quy trinh khac nhau (4.7).",
        cxn="Engine workflow cụ thể? Có version workflow không?",
    ),
    dict(
        us_id="US-APR-02",
        ten="Phe duyet buoc hien tai",
        story="Là người được giao ở bước hiện tại, tôi muốn phê duyệt hồ sơ. Kiểm tra role là chưa đủ.",
        muc="4.7; APR-01 APR-02 APR-03 APR-05; 5.5 race",
        trang="3, 5",
        actor="Assignee buoc hien tai. BGD/Phap che/Kinh doanh tuy cau hinh.",
        pre="Ho so dang o buoc cua actor. Actor dung la assignee (APR-01).",
        main="1) Assignee approve.\n2) Khong nhay buoc, khong duyet lai buoc da xong (APR-02).\n3) Buoc cuoi approve -> ho so Approved; co the phat sinh event gui ky (APR-05).",
        alt="A1. Khong phai assignee (ke ca Manager khac) -> khong duyet (APR-01, 5.5 ngu canh).\nA2. Hai request approve cung luc khong hoan thanh buoc hai lan (5.5 Race) — ky thuat.\nA3. Comment: APR-03 bat comment/ly do neu reject/request revision; approve thuong: Cần xác nhận co bat buoc comment khong.",
        rules="APR-01, APR-02, APR-03, APR-05.",
        ac="AC1: Chi assignee buoc hien tai duyet duoc.\nAC2: Khong nhay buoc / khong duyet lai buoc xong.\nAC3: Buoc cuoi -> Approved (+ event ky neu co).",
        cxn="Approve có bắt buộc comment không (APR-03 chỉ nêu reject/request revision)?",
    ),
    dict(
        us_id="US-APR-03",
        ten="Tu choi ho so",
        story="Là assignee bước hiện tại, tôi muốn từ chối hồ sơ kèm lý do. Hồ sơ kết thúc Rejected hoặc về Revision theo quy tắc được thiết kế.",
        muc="4.7; APR-01 APR-03 APR-04; CTR-04; PRC-06",
        trang="3, 4, 5",
        actor="Assignee buoc hien tai",
        pre="APR-01.",
        main="Reject kem comment/ly do (APR-03).",
        alt="APR-04: ket thuc Rejected HOAC quay ve Revision — Cần xác nhận chon mot quy tac. CTR-04: HĐ Rejected khong tu dong sua+submit.",
        rules="APR-01, APR-03, APR-04, CTR-04, PRC-06 (bang gia, dieu kien).",
        ac="AC1: Reject phai co ly do (APR-03).\nAC2: Chi assignee thuc hien duoc.\nTrang thai cuoi: Cần xác nhận (APR-04 hai nhanh).",
        cxn="Chốt Rejected vs Revision theo loại hồ sơ?",
    ),
    dict(
        us_id="US-APR-04",
        ten="Yeu cau chinh sua",
        story="Là assignee bước hiện tại, tôi muốn yêu cầu chỉnh sửa hồ sơ kèm lý do.",
        muc="4.7; APR-01 APR-03; CTR-01 Revision Requested",
        trang="3-5",
        actor="Assignee buoc hien tai",
        pre="APR-01.",
        main="Request revision + comment/ly do (APR-03). Hop dong: trang thai Revision Requested cho phep sua (CTR-01).",
        alt="Cần xác nhận ho so quay dung buoc nao.",
        rules="APR-01, APR-03, CTR-01.",
        ac="AC1: Request revision bat ly do.\nAC2: HĐ o Revision Requested thi duoc sua (CTR-01).",
        cxn="Quay về bước đầu hay bước nộp? Có hạn chỉnh sửa không?",
    ),
    dict(
        us_id="US-APR-05",
        ten="Theo doi tien do phe duyet",
        story="Là người dùng liên quan hồ sơ, tôi muốn xem người đang xử lý, bước đã xong và bước còn lại.",
        muc="4.7; 4.2; 4.10",
        trang="3",
        actor="Nguoi dung (4.7). Cần xác nhận pham vi quyen xem.",
        pre="Ho so da vao quy trinh hoac Cần xác nhận khi chua gui.",
        main="Hien thi nguoi dang xu ly, buoc hoan thanh, buoc con lai.",
        alt="Cần xác nhận.",
        rules="Khong ma rieng.",
        ac="AC: Hien thi du 3 nhom thong tin muc 4.7.",
        cxn="Người không tham gia hồ sơ có xem được không?",
    ),
    dict(
        us_id="US-ESN-01",
        ten="Gui ho so sang ky dien tu",
        story="Sau khi hồ sơ được phê duyệt nội bộ, hệ thống có thể gửi hồ sơ sang dịch vụ ký điện tử. Bảng thanh toán chỉ gửi ký sau khi Approved nội bộ.",
        muc="3 buoc 7; 4.8; PAY-06; APR-05",
        trang="2, 3, 5",
        actor="Cần xác nhận ai bam gui ky. He thong co the phat sinh tu APR-05.",
        pre="Da Approved noi bo. PAY-06 bat buoc voi bang thanh toan. 4.8: sau phe duyet noi bo.",
        main="Gui sang dich vu ky. Trang thai phien ky: cho gui ky, dang ky, ky thanh cong, ky that bai, huy ky (4.8). Tach trang thai ky vs phe duyet (5.5 Tich hop ky dien tu).",
        alt="A1. Chua Approved -> bang thanh toan khong duoc gui ky (PAY-06).\nA2. Loi E-Sign tam thoi: khong lam hong du lieu da duyet; retry hoac trang thai cho (APR-07).",
        rules="PAY-06, APR-05, APR-06, APR-07, PAY-07.",
        ac="AC1: Thanh toan chi gui ky sau Approved (PAY-06).\nAC2: Co mo hinh trang thai phien ky liet ke 4.8.\nKhong yeu cau chu ky so hop le phap ly (4.8).",
        cxn="Hợp đồng/bảng giá có bắt buộc e-sign như thanh toán không? PAY-06 chỉ nói thanh toán. Actor kích hoạt gửi ký?",
    ),
    dict(
        us_id="US-ESN-02",
        ten="Cap nhat ket qua ky bat dong bo",
        story="Dịch vụ ký xử lý bất đồng bộ (callback/webhook); hệ thống cập nhật trạng thái ký. Thất bại/hủy phải phản ánh rõ để xử lý lại.",
        muc="4.8; APR-06; PAY-07",
        trang="3, 5",
        actor="He thong / dich vu ky (khong phai phong ban).",
        pre="Phien ky da duoc tao.",
        main="Nhan callback/webhook; cap nhat trang thai ky tuong ung (APR-06).",
        alt="Ky that bai hoac huy: trang thai ro de xu ly lai (PAY-07). Khong tron voi trang thai phe duyet (5.5).",
        rules="APR-06, PAY-07.",
        ac="AC1: Cap nhat duoc cac trang thai 4.8.\nAC2: Fail/huy nhin ro, xu ly lai duoc (PAY-07).",
        cxn="Mô hình mô phỏng hay tích hợp bên thứ ba (4.8 để sinh viên đề xuất — không chốt trong DATH).",
    ),
    dict(
        us_id="US-NTF-01",
        ten="Nhan va xem thong bao",
        story="Là người dùng, tôi muốn được thông báo khi có hồ sơ cần xử lý, từ chối, được duyệt, ký xong, HĐ hoặc bảng giá sắp hết hạn; và xem danh sách thông báo của mình.",
        muc="4.9; APR-07",
        trang="3, 5",
        actor="Nguoi dung nhan thong bao. Notification Service nhan event bat dong bo (4.9) — de xuat kien truc.",
        pre="Cần xác nhận dang nhap.",
        main="He thong phat thong bao cac su kien liet ke 4.9. Nguoi dung xem danh sach cua minh.",
        alt="Notification loi tam thoi: nghiep vu chinh khong hong du lieu da duyet (APR-07).",
        rules="APR-07. 4.9 liet ke loai su kien.",
        ac="AC: Co thong bao cho cac su kien: can xu ly, tu choi, duyet, ky xong, HĐ/bang gia sap het han. User xem list cua minh.",
        cxn="'Sắp hết hạn' là bao nhiêu ngày? Có thông báo phụ lục không?",
    ),
    dict(
        us_id="US-NTF-02",
        ten="Danh dau thong bao da doc",
        story="Là người dùng, tôi muốn đánh dấu thông báo đã đọc.",
        muc="4.9",
        trang="3",
        actor="Nguoi dung so huu thong bao",
        pre="Thong bao ton tai va thuoc ve user.",
        main="Danh dau da doc.",
        alt="Cần xác nhận danh dau hang loat / chua doc lai.",
        rules="Khong ma.",
        ac="AC: User danh dau da doc thong bao cua minh (4.9).",
        cxn="Có bắt buộc đọc mới xử lý hồ sơ không? DATH không nói.",
    ),
    dict(
        us_id="US-AUD-01",
        ten="Nhat ky va truy vet",
        story="Tôi muốn tra cứu lịch sử theo hợp đồng, bảng giá, bảng thanh toán và phiên ký: ai, thời điểm, hành động, trạng thái trước/sau, ghi chú. Audit không phụ thuộc dữ liệu hiển thị hiện tại.",
        muc="4.10; 5.5 Du lieu lich su; PAY-03",
        trang="3, 6",
        actor="Cần xác nhận ai duoc xem audit (Kinh doanh/Quan tri/tat ca?).",
        pre="Da co hanh dong tren ho so.",
        main="Ghi va tra cuu audit theo HĐ, bang gia, thanh toan, phien ky.",
        alt="Cần xác nhận.",
        rules="4.10. PAY-03/5.5: don gia thanh toan luu tai thoi diem tinh.",
        ac="AC1: Ban ghi gom nguoi, thoi diem, hanh dong, trang thai truoc/sau, ghi chu.\nAC2: Tra cuu theo 4 loai doi tuong muc 4.10.\nAC3: Khong mat vet khi du lieu hien thi doi.",
        cxn="Thời gian lưu audit? Khách hàng/sản lượng có audit bắt buộc không (4.10 không liệt kê)?",
    ),
    dict(
        us_id="US-ADM-01",
        ten="Quan ly nguoi dung, phan quyen, loai ho so",
        story="Là quản trị hệ thống, tôi muốn quản lý người dùng, phân quyền, cấu hình loại hồ sơ (và workflow — US-APR-01).",
        muc="2 Quan tri he thong",
        trang="2",
        actor="Quan tri he thong",
        pre="Cần xác nhận.",
        main="Quan ly user, phan quyen, cau hinh loai ho so.",
        alt="Cần xác nhận.",
        rules="APR-01: phan quyen theo assignee, khong chi role. 5.5 ngu canh.",
        ac="AC: He thong ho tro quan ly user, quyen, loai ho so (muc 2). Chi tiet model: Cần xác nhận.",
        cxn="Mô hình role/permission? Gắn user vào phòng ban?",
    ),
    dict(
        us_id="US-ACC-01",
        ten="Theo doi cong no",
        story="Là nhân viên Kế toán, tôi muốn theo dõi công nợ.",
        muc="2 Ke toan (vai tro)",
        trang="2",
        actor="Ke toan",
        pre="Cần xác nhận phu thuoc bang thanh toan da ky?",
        main="Cần xác nhận: DATH chi liet ke vai tro, khong co muc chuc nang cong no.",
        alt="Cần xác nhận.",
        rules="Khong ma.",
        ac="Cần xác nhận — khong co AC trong DATH.",
        cxn="Toàn bộ phạm vi công nợ (phát sinh, đối trừ, tuổi nợ) không có trong mục 4. Không tự thiết kế.",
    ),
    dict(
        us_id="US-ARC-01",
        ten="Phat hanh va luu tru ho so sau khi ky",
        story="Sau khi ký hoàn tất, hồ sơ được phát hành và lưu trữ.",
        muc="3 buoc 8",
        trang="2",
        actor="Cần xác nhận.",
        pre="Ky hoan tat (muc 3.8).",
        main="Phat hanh va luu tru. Khong mo ta buoc, dinh dang, noi luu.",
        alt="Cần xác nhận ky that bai (khong phat hanh).",
        rules="Khong ma rieng. Trang thai ky 4.8.",
        ac="Cần xác nhận chi tiet 'phat hanh' va 'luu tru'.",
        cxn="Phát hành = đổi trạng thái Issued? Lưu trữ file ở đâu? Ai tải?",
    ),
    dict(
        us_id="US-CTR-07",
        ten="Hieu luc hop dong Approved -> Active",
        story="Hợp đồng Approved chỉ chuyển Active khi đến ngày hiệu lực.",
        muc="5.1 CTR-05",
        trang="4",
        actor="He thong (theo ngay). Cần xác nhận co job/lich.",
        pre="Hop dong Approved. Da den ngay hieu luc (CTR-05).",
        main="Chuyen Active khi den ngay hieu luc.",
        alt="Cần xác nhận neu ngay hieu luc trong qua khu luc moi duyet.",
        rules="CTR-05.",
        ac="AC: Approved khong Active truoc ngay hieu luc (CTR-05).",
        cxn="Tự động hay người bấm kích hoạt? Múi giờ/ngày hệ thống?",
    ),
]

# 02 danh sach
ws = wb.create_sheet("02_Danh_sach_US")
dump(
    ws,
    ["US_ID", "Ten", "Nhom", "Muc_DATH", "Trang", "Actor", "User_Story_rut_gon"],
    [
        [
            s["us_id"],
            s["ten"],
            s["us_id"].split("-")[1],
            s["muc"],
            s["trang"],
            s["actor"],
            s["story"],
        ]
        for s in stories
    ],
    [14, 42, 10, 28, 12, 40, 80],
)

# 03 chi tiet
ws = wb.create_sheet("03_Chi_tiet_US")
headers = [
    "US_ID",
    "Ten",
    "User_Story",
    "Muc_DATH",
    "Trang_PDF",
    "Actor",
    "Precondition",
    "Main_flow",
    "Alternative_flow",
    "Business_rules",
    "Acceptance_criteria",
    "Can_xac_nhan",
    "Tai_lieu",
]
dump(
    ws,
    headers,
    [
        [
            s["us_id"],
            s["ten"],
            s["story"],
            s["muc"],
            s["trang"],
            s["actor"],
            s["pre"],
            s["main"],
            s["alt"],
            s["rules"],
            s["ac"],
            s["cxn"],
            SRC,
        ]
        for s in stories
    ],
    [14, 36, 50, 22, 12, 36, 40, 50, 50, 36, 50, 50, 18],
)
for r in range(2, len(stories) + 2):
    ws.row_dimensions[r].height = 120

# 04 rules
ws = wb.create_sheet("04_Business_Rules")
rules_rows = [
    ["CTR-01", "Hop dong", "Chi duoc chinh sua hop dong o Draft hoac Revision Requested.", "5.1", "4", "US-CTR-02, US-APR-04"],
    ["CTR-02", "Hop dong", "Chi Submit khi khach hang hop le, thoi gian hieu luc hop le, it nhat mot tep/hang muc noi dung bat buoc.", "5.1", "4", "US-CTR-03"],
    ["CTR-03", "Hop dong", "Khong chuyen truc tiep Draft sang Approved; phai qua quy trinh phe duyet.", "5.1", "4", "US-CTR-03"],
    ["CTR-04", "Hop dong", "Rejected khong duoc tu dong sua va submit lai; can tao ban chinh sua hoac chuyen ve Revision theo quy tac nhom thiet ke.", "5.1", "4", "US-CTR-03, US-APR-03. Cần xác nhận nhanh nao."],
    ["CTR-05", "Hop dong", "Approved chi chuyen Active khi den ngay hieu luc.", "5.1", "4", "US-CTR-07"],
    ["CTR-06", "Hop dong", "Active khong duoc xoa; khong dung nua phai Cancelled hoac Expired theo quy tac nghiep vu.", "5.1", "4", "US-CTR-06"],
    ["CTR-07", "Hop dong", "Active/Approved thay doi dieu khoan quan trong phai tao phu luc, khong sua truc tiep.", "5.1", "4", "US-CTR-02, US-ADD-01"],
    ["PRC-01", "Bang gia", "Phai gan KH, HĐ, nhom DV hoac pham vi ap dung ro.", "5.2", "4", "US-PRC-01"],
    ["PRC-02", "Bang gia", "Phai co thoi gian hieu luc; start khong lon hon end.", "5.2", "4", "US-PRC-01"],
    ["PRC-03", "Bang gia", "Khong hai Effective chong thoi gian cho cung doi tuong va cung loai DV.", "5.2", "4", "US-PRC-02"],
    ["PRC-04", "Bang gia", "Tao version moi: version cu Superseded hoac het hieu luc theo ngay.", "5.2", "4", "US-PRC-02"],
    ["PRC-05", "Bang gia", "Da dung sinh bang thanh toan thi khong sua truc tiep; phai version moi.", "5.2", "4", "US-PRC-02"],
    ["PRC-06", "Bang gia", "Rejected co the sua va submit lai neu nhom thiet ke cho phep.", "5.2", "4", "US-PRC-03. Cần xác nhận."],
    ["PAY-01", "Thanh toan", "Chi lap khi HĐ con hieu luc va co bang gia phu hop tai ky tinh phi.", "5.3", "5", "US-PAY-01"],
    ["PAY-02", "Thanh toan", "San luong thuoc ky va da xac nhan/doi soat theo quy tac nhom thiet ke.", "5.3", "5", "US-PAY-01, US-VOL-03. Cần xác nhận quy tac."],
    ["PAY-03", "Thanh toan", "Luu don gia tai thoi diem tinh phi.", "5.3", "5", "US-PAY-01, US-AUD-01"],
    ["PAY-04", "Thanh toan", "Khong submit neu tong tien am hoac thieu dong DV bat buoc.", "5.3", "5", "US-PAY-03"],
    ["PAY-05", "Thanh toan", "Sau Approved hoac Signed khong sua truc tiep; dieu chinh hoac huy theo quy trinh.", "5.3", "5", "US-PAY-02, US-PAY-04"],
    ["PAY-06", "Thanh toan / ky", "Chi gui ky dien tu sau Approved noi bo.", "5.3", "5", "US-ESN-01"],
    ["PAY-07", "Thanh toan / ky", "Ky that bai hoac huy: trang thai phai ro de xu ly lai.", "5.3", "5", "US-ESN-02"],
    ["APR-01", "Phe duyet", "Chi assignee buoc hien tai duoc approve/reject/request revision. Role chua du.", "5.4", "5", "US-APR-02..04"],
    ["APR-02", "Phe duyet", "Khong duyet nhay buoc hoac duyet lai buoc da xong.", "5.4", "5", "US-APR-02"],
    ["APR-03", "Phe duyet", "Moi hanh dong phe duyet phai ghi comment hoac ly do neu reject/request revision.", "5.4", "5", "US-APR-02..04. Cần xác nhận comment khi approve."],
    ["APR-04", "Phe duyet", "Reject: ket thuc Rejected hoac ve Revision theo quy tac thiet ke.", "5.4", "5", "US-APR-03. Cần xác nhận."],
    ["APR-05", "Phe duyet / ky", "Buoc cuoi approve -> Approved; co the event gui ky.", "5.4", "5", "US-APR-02, US-ESN-01"],
    ["APR-06", "Ky dien tu", "Ky bat dong bo callback/webhook; cap nhat trang thai ky.", "5.4", "5", "US-ESN-02"],
    ["APR-07", "Thong bao / ky", "Neu Notification hoac E-Sign loi tam thoi, khong lam hong du lieu da duyet; retry hoac trang thai cho.", "5.4", "5", "US-ESN-01, US-NTF-01"],
]
dump(
    ws,
    ["Ma_rule", "Nhom", "Noi_dung", "Muc", "Trang", "US_lien_quan_va_ghi_chu"],
    rules_rows,
    [12, 18, 70, 10, 10, 50],
)
for r in range(2, len(rules_rows) + 2):
    ws.row_dimensions[r].height = 48

# 05 ky thuat — not business
ws = wb.create_sheet("05_De_xuat_ky_thuat")
dump(
    ws,
    ["Muc", "Trang", "Van_de", "Noi_dung_trong_DATH", "Phan_loai", "Luu_y_BA"],
    [
        ["5.5", "5", "Double submit", "Bam Submit nhieu lan khong tao nhieu workflow instance. Khuyen khich Idempotency-Key hoac unique constraint.", "Rang buoc gan rule + de xuat ky thuat", "Hanh vi 'khong nhan doi workflow' la yeu cau. Idempotency-Key la de xuat, khong phai rule nghiep vu moi."],
        ["5.5", "5", "Race duyet", "Hai request approve cung luc khong hoan thanh buoc hai lan. Transaction / row-lock / optimistic lock.", "Ky thuat", "Khong them rule nghiep vu. Gan APR-02."],
        ["5.5", "6", "Event bi mat", "Outbox Pattern hoac retry khi cap nhat trang thai va gui event.", "Ky thuat", "Gan APR-05, 4.9."],
        ["5.5", "6", "Phan quyen ngu canh", "Manager A khong duyet ho so Manager B neu khong phai assignee.", "Lam ro APR-01", "Ghi vao US-APR-02, khong tao ma rule moi."],
        ["5.5", "6", "Du lieu lich su", "Bang thanh toan luu don gia tai thoi diem tinh, khong phu thuoc bang gia hien tai.", "Trung PAY-03", "Khong tao rule moi."],
        ["5.5", "6", "Tich hop ky dien tu", "Mo hinh trang thai rieng cho phien ky; khong tron phe duyet va ky.", "Thiet ke trang thai", "Gan 4.8, US-ESN-01."],
        ["4.7", "3", "Workflow engine", "Quy trinh khong hard-code if/else don gian.", "Yeu cau thiet ke", "Khong suy dien product workflow cu the."],
        ["4.8", "3", "E-sign", "Sinh vien tu nghien cuu mo phong hoac ben thu 3. Khong yeu cau chu ky hop le phap ly.", "Pham vi do an", "Cần xác nhận chon mo hinh."],
        ["4.9", "3", "Notification Service", "Nen nhan event bat dong bo tu service khac.", "De xuat kien truc", "Khong bat buoc stack cu the."],
        ["6", "6", "Stack", "Web API, .NET Core, C#, PostgreSQL; AI Agent; Gitlab; UML; Figma.", "Yeu cau ky thuat do an", "Ngoai pham vi US nghiep vu."],
        ["5 mo dau", "4", "Trang thai toi thieu", "Nhom duoc phep dieu chinh/mo rong trang thai neu giai thich trong thiet ke va demo.", "Luu y sinh vien", "BA khong tu mo rong trong phan tich nay."],
    ],
    [10, 10, 24, 70, 28, 50],
)
for r in range(2, 13):
    ws.row_dimensions[r].height = 56

# 06 Can xac nhan tong hop
cxn_rows = [
    ["CXN-01", "Chung", "DATH khong danh so User Story; US_ID do BA dat de truy vet. Reviewer xac nhan granule (gop/tach)."],
    ["CXN-02", "Chung", "docs/business-rules.md khong con trong repo; chi dung muc 5 cua DATH."],
    ["CXN-03", "US-CTR-03", "Ten trang thai sau Submit khong dat trong DATH (chi cam Draft->Approved)."],
    ["CXN-04", "US-CTR-03 / CTR-02", "Danh muc tep/hang muc noi dung bat buoc theo loai hop dong."],
    ["CXN-05", "US-CTR-03", "Ai duoc Submit: chi nguoi tao hay moi Kinh doanh duoc phan quyen."],
    ["CXN-06", "CTR-04 / APR-04 / PRC-06 / PAY-02", "Nhieu rule de 'quy tac nhom thiet ke' — chua chot."],
    ["CXN-07", "CTR-07", "Danh muc 'dieu khoan quan trong'."],
    ["CXN-08", "CTR-02 / PRC-02", "'Thoi gian hieu luc hop le' cua HĐ: chi start<=end hay them rang ngay hien tai?"],
    ["CXN-09", "US-CTR-05", "Gia han = phu luc hay sua HĐ? Co phe duyet lai?"],
    ["CXN-10", "US-CTR-06", "Expired tu dong hay thao tac? Ai duoc Huy?"],
    ["CXN-11", "US-CUS-03", "Tam ngung KH co chan HĐ/bang gia/thanh toan moi?"],
    ["CXN-12", "US-PRC-01", "Muc 3.3: tao bang gia sau HĐ duyet — bat buoc he thong hay chi quy trinh thu cong?"],
    ["CXN-13", "US-PRC-02", "Dinh nghia doi tuong ap dung, loai DV, overlapping bien ngay."],
    ["CXN-14", "US-VOL-03 / PAY-02", "Khoa ky vs xac nhan/doi soat; ai khoa; quyen dac biet."],
    ["CXN-15", "US-PAY-03", "Dong dich vu bat buoc; tong tien = 0."],
    ["CXN-16", "US-ESN-01", "E-sign bat buoc cho HĐ/bang gia hay chi thanh toan (PAY-06)?"],
    ["CXN-17", "US-ESN-02", "Mo phong hay tich hop vendor (4.8 de xuat)."],
    ["CXN-18", "US-NTF-01", "Nguong 'sap het han'."],
    ["CXN-19", "US-ACC-01", "Theo doi cong no chi co o muc 2, khong co muc 4 — pham vi?"],
    ["CXN-20", "US-ARC-01", "Phat hanh va luu tru: trang thai, kho luu, quyen tai."],
    ["CXN-21", "US-ADM-01", "Mo hinh user/role/phong ban."],
    ["CXN-22", "US-APR-02", "Approve co bat buoc comment? APR-03 chi noi ro reject/request revision."],
    ["CXN-23", "US-CTR-07", "Chuyen Active: job tu dong hay thu cong."],
    ["CXN-24", "4.7", "Hien thi han xu ly buoc — DATH khong noi."],
    ["CXN-25", "Auth", "Dang nhap, session, SSO — DATH khong mo ta; khong suy dien vao precondition ngoai Cần xác nhận."],
]
ws = wb.create_sheet("06_Can_xac_nhan")
dump(ws, ["Ma", "Pham_vi", "Noi_dung_can_reviewer_chot"], cxn_rows, [12, 24, 100])
for r in range(2, len(cxn_rows) + 2):
    ws.row_dimensions[r].height = 36
    ws.cell(r, 3).fill = fill_note

# 07 quy trinh
ws = wb.create_sheet("07_Quy_trinh_tong_quat")
dump(
    ws,
    ["Buoc", "Mo_ta", "US_lien_quan", "Can_cu"],
    [
        ["1", "Kinh doanh tao thong tin KH va ho so HĐ.", "US-CUS-01, US-CTR-01", "Muc 3, trang 2"],
        ["2", "HĐ gui luong ra soat/phe duyet Kinh doanh, Phap che, BGD.", "US-CTR-03, US-APR-02..05", "Muc 3, trang 2"],
        ["3", "Sau HĐ duyet, Kinh doanh hoac bo phan phu trach tao bang gia.", "US-PRC-01", "Muc 3, trang 2"],
        ["4", "Bang gia phe duyet va hieu luc theo thoi gian.", "US-PRC-03", "Muc 3, trang 2"],
        ["5", "Khai thac ghi nhan san luong theo ky.", "US-VOL-01", "Muc 3, trang 2"],
        ["6", "Ke toan lap bang thanh toan tu HĐ, bang gia, san luong.", "US-PAY-01", "Muc 3, trang 2"],
        ["7", "Bang thanh toan doi soat, trinh duyet, gui ky dien tu.", "US-PAY-02, US-PAY-03, US-ESN-01", "Muc 3, trang 2"],
        ["8", "Sau ky hoan tat: phat hanh va luu tru.", "US-ARC-01", "Muc 3, trang 2"],
    ],
    [10, 70, 40, 22],
)

wb.save(OUT)
print("Wrote", OUT)
