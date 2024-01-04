from app.models import BacSi, BenhNhan, DKKham, DSCaKham, PhieuKhamBenh, Thuoc, DonVi, DanhMuc, ChiTietDonThuoc, User
from app import app, db
import hashlib
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


def test_patient(hoten):
    # Check if the patient with the given name exists in the BenhNhan table
    patient = BenhNhan.query.filter_by(hoten=hoten).first()

    if patient:
        return True
    else:
        return False


def count_quantity():
    count_quantity = db.session.query(Thuoc.id,
                                      Thuoc.tenthuoc,
                                      DonVi.loaidonvi,
                                      func.coalesce(func.cast(func.sum(ChiTietDonThuoc.soluong), Integer), 0)
                                      ).join(DonVi, DonVi.id == Thuoc.donvi_id, isouter=True)\
                                       .join(ChiTietDonThuoc, ChiTietDonThuoc.thuoc_id == Thuoc.id, isouter=True)\
                                       .group_by(Thuoc.id)
    return count_quantity.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.tendangnhap.__eq__(username), User.MatKhau.__eq__(password)).first()

def get_add_detailDrug(nameDrg, frmId, Quantity):
    thuoc = Thuoc.query.filter_by(tenthuoc=nameDrg).first()
    phieu = PhieuKhamBenh.query.filter_by(id=frmId).first()
    dtls = ChiTietDonThuoc(soluong=Quantity, thuoc_id=thuoc.id, phieu_id=phieu.id)

    db.session.add(dtls)
    db.session.commit()

    return True


if __name__ == '__main__':
    with (app.app_context()):
        pass










