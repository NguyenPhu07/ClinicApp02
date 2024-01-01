from app.models import BacSi, BenhNhan, DKKham, DSCaKham, PhieuKhamBenh, Thuoc, DonVi, DanhMuc, ChiTietDonThuoc
from app import app, db
from sqlalchemy import func, Integer


def get_bacsi():
    return BacSi.query.all()

def add_patient_register(name, phone, gender, date, address, reason):
    u = BenhNhan(hoten=name, sdt=phone, ngaysinh=date, GioiTinh=gender, diachi=address)
    db.session.add(u)
    db.session.commit()

    b = DKKham(lydokham=reason, bn_id = u.id)
    db.session.add(b)
    db.session.commit()

    return True

def count_quantity():
    count_quantity = db.session.query(Thuoc.id,
                                      Thuoc.tenthuoc,
                                      DonVi.loaidonvi,
                                      func.coalesce(func.cast(func.sum(ChiTietDonThuoc.soluong), Integer), 0)
                                      ).join(DonVi, DonVi.id == Thuoc.donvi_id, isouter=True)\
                                       .join(ChiTietDonThuoc, ChiTietDonThuoc.thuoc_id == Thuoc.id, isouter=True)\
                                       .group_by(Thuoc.id)
    return count_quantity.all()

if __name__ == '__main__':
    with (app.app_context()):
        print(count_quantity())






