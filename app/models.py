from sqlalchemy import Column, Integer, String, DateTime, Float ,Boolean, VARCHAR, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
from app import db, app
import enum
from datetime import datetime


class UserRoleEnum(enum.Enum):
    ADMIN = 1
    DOCTOR = 2
    NURSE = 3
    CASHIER = 4


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tendangnhap = Column(String(50), nullable=False, unique=True)
    MatKhau = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.DOCTOR)
    DSbacsi = relationship('BacSi', uselist=False, backref= 'users', lazy=True)
    DSadmin = relationship('Admin', uselist=False, backref='users', lazy=True)
    DSyta = relationship('YTa', uselist=False, backref='users', lazy=True)
    DSthungan = relationship('ThuNgan', uselist=False, backref='users', lazy=True)


class BacSi(db.Model):
    __tablename__ = 'bacsi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False, unique=True)
    sdt = Column(String(50), nullable=False)
    chuyenkhoa = Column(String(50), nullable=False, unique=False)
    SoChungChiHanhNghe = Column(String(50), nullable=False)
    avatar = Column(VARCHAR(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    listkham = relationship('DSCaKham', backref='bacsi', lazy=True)
    DSPhieuKham = relationship('PhieuKhamBenh', backref='bacsi', lazy=True)#-------


class Admin(db.Model):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False, unique=True)
    sdt = Column(String(50), nullable=False)
    trangthaitk = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

class YTa(db.Model):
    __tablename__ = 'yta'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False, unique=True)
    sdt = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

class ThuNgan(db.Model):
    __tablename__ = 'thungan'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False, unique=True)
    sdt = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    DSdalaphd = relationship('HoaDon', backref='thungan', lazy=True)



class BenhNhan(db.Model):
    __tablename__ = 'benhnhan'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False, unique=True)
    sdt = Column(String(50), nullable=False)
    ngaysinh = Column(DateTime, nullable=False)
    diachi = Column(VARCHAR(50))
    GioiTinh = Column(String(50), nullable=False)
    DSdk = relationship('DKKham', backref='benhnhan', lazy=True)
    DScadikham = relationship('DSCaKham', backref='benhnhan', lazy=True)
    DSPhieuKham = relationship('PhieuKhamBenh', backref='benhnhan', lazy=True) #--------
    DSHoaDonThanhToan = relationship('HoaDon', backref='benhnhan', lazy=True)#------


class DKKham(db.Model):
    __tablename__ = 'dangkykham'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lydokham = Column(VARCHAR(50), nullable=False, unique=False)
    ngaydk = Column(DateTime, default=datetime.now())
    bn_id = Column(Integer, ForeignKey(BenhNhan.id), nullable=False)


class DSCaKham(db.Model):
    __tablename__ = 'dscakham'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trangthaica = Column(String(50), nullable=False)
    ngaykham = Column(DateTime, default=datetime.now())
    phongkham = Column(String(50)) #-------new-----------------
    bs_id = Column(Integer, ForeignKey(BacSi.id), nullable=False)
    bn_id = Column(Integer, ForeignKey(BenhNhan.id), nullable=False)

#------------new------------------------
class PhieuKhamBenh(db.Model):
    __tablename__ = 'phieukhambenh'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngaykham = Column(DateTime, default=datetime.now())
    trieuchung = Column(String(100))
    chandoan = Column(String(100))
    bn_id = Column(Integer, ForeignKey(BenhNhan.id), nullable=False)
    bs_id = Column(Integer, ForeignKey(BacSi.id), nullable=False)
    DSHoaDon = relationship('HoaDon', uselist=False, backref='phieukhambenh', lazy=True)
    DSThuoc = relationship('ChiTietDonThuoc', backref='phieukhambenh', lazy=True)#--------------


#------------new------------------------
class HoaDon(db.Model):
    __tablename__ = 'hoadon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tienkham = Column(Float, default=0)
    tienthuoc = Column(Float, default=0)
    trangthai = Column(String(50), nullable=False)
    NgayPhatSinh = Column(DateTime, default=datetime.now())
    bn_id = Column(Integer, ForeignKey(BenhNhan.id), nullable=False)
    phieu_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False)
    tn_id = Column(Integer, ForeignKey(ThuNgan.id), nullable=False)

#------------------new-----------------
class DonVi(db.Model):
    __tablename__ = 'donvi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    loaidonvi = Column(String(50), nullable=False, unique=True)
    DSThuoc = relationship('Thuoc', backref='donvi',lazy=True)

#---------------new-----------------------
class DanhMuc(db.Model):
    __tablename__ = 'danhmuc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(50), nullable=False, unique=True)


#----------------new------------------
class Thuoc(db.Model):
    __tablename__ = 'thuoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenthuoc = Column(String(50), nullable=False, unique=True)
    gia = Column(Float, default=0)
    cachdung = Column(VARCHAR(50), nullable=False, unique=False)
    donvi_id = Column(Integer, ForeignKey(DonVi.id), nullable=False)
    DSPhieuKham = relationship('ChiTietDonThuoc', backref='thuoc', lazy=True)#-------------
    DSDanhmuc = relationship('DanhMuc', secondary='danhmuc_thuoc' , lazy='subquery',
                             backref=backref('DSThuoc', lazy = True))

#-----------------new-midle-table---------------------
danhmuc_thuoc = db.Table('danhmuc_thuoc',
                         Column('danhmuc_id',Integer,ForeignKey('danhmuc.id'), primary_key=True),
                         Column('thuoc_id',Integer, ForeignKey('thuoc.id'), primary_key=True))


#-----------------new-midle-table---------------------
class ChiTietDonThuoc(db.Model):
    __tablename__ = 'chitietdonthuoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    soluong = Column(Integer, default=0)
    phieu_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False)
    thuoc_id = Column(Integer, ForeignKey(Thuoc.id), nullable=False)





if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()

        # u1 = User(tendangnhap='Thanh', MatKhau='123456', user_role=UserRoleEnum.DOCTOR)
        # db.session.add(u1)
        # db.session.commit()
        #
        # u2 = User(tendangnhap='DKhanhtv123', MatKhau='123456', user_role=UserRoleEnum.DOCTOR)
        # db.session.add(u2)
        # db.session.commit()
        # u3 = User(tendangnhap='bsLan', MatKhau='123456', user_role=UserRoleEnum.DOCTOR)
        # u4 = User(tendangnhap='bsPhuoc', MatKhau='123456', user_role=UserRoleEnum.DOCTOR)
        # u5 = User(tendangnhap='bsCKIThuy', MatKhau='123456', user_role=UserRoleEnum.DOCTOR)
        # u6 = User(tendangnhap='bsTien', MatKhau='123456', user_role=UserRoleEnum.DOCTOR)
        # u7 = User(tendangnhap='calieKim', MatKhau='123456', user_role=UserRoleEnum.CASHIER)
        # db.session.add_all([u3, u4, u5, u6,u7])
        # db.session.commit()
        # #
        # b1 = BacSi(hoten='BS. Ho Van Thanh', sdt='091278245', chuyenkhoa='Nội sản',
        #            SoChungChiHanhNghe='TN-0123', user_id=1)
        # b2 = BacSi(hoten='BS. Trương thị diễm khanh', sdt='09343425', chuyenkhoa='Khoa Nhi',
        #            SoChungChiHanhNghe='TN-0124', user_id=2)
        # db.session.add(b1)
        # db.session.add(b2)
        # db.session.commit()
        # ## add bệnh nhân trên triển khai web do làm biếng


        # thungan1 = ThuNgan(hoten='Kim Ngân', sdt='093434345', user_id=7)
        # db.session.add(thungan1)
        # db.session.commit()
        #
        # #add danh sách ca khám do y tá
        #
        # phieukham1 = PhieuKhamBenh(trieuchung='sốt nhẹ', chandoan='Viêm amidan', bn_id= 2, bs_id = 1)
        # db.session.add(phieukham1)
        # db.session.commit()
        #
        # phieukham2 = PhieuKhamBenh(trieuchung='chảy nước mũi', chandoan='Viêm mũi nhẹ', bn_id=1, bs_id=1)
        # db.session.add(phieukham2)
        # db.session.commit()
        #
        # vy = DonVi(loaidonvi='vỹ')
        # chai = DonVi(loaidonvi='Chai')
        # vien = DonVi(loaidonvi='Viên')
        # db.session.add_all([vy,chai,vien])
        # db.session.commit()


        # add danh mục r add thuốc r test bảng trung gian danhmuc_thuoc
        # d1 = DanhMuc(ten='Giảm cân')
        # d2 = DanhMuc(ten='Kháng Sinh')
        # d3 = DanhMuc(ten='Em bé')
        # d4 = DanhMuc(ten='Thuốc gây mê')
        # db.session.add_all([d1,d2,d3,d4])
        # db.session.commit()

        # thuoc1 = Thuoc(tenthuoc='Dimadrol', gia=4000, cachdung='2 lần sáng chiều', donvi_id=1)
        # thuoc2 = Thuoc(tenthuoc='Panactol', gia=4000, cachdung='2 lần chiều', donvi_id=2)
        # thuoc3 = Thuoc(tenthuoc='Neucotic', gia=4000, cachdung='1 lần sáng tối', donvi_id=1)
        # thuoc4 = Thuoc(tenthuoc='Dimadrol-3', gia=4000, cachdung='2 lần sáng chiều', donvi_id=1)
        # thuoc5 = Thuoc(tenthuoc='Neocin', gia=4000, cachdung='3 lần sáng chiều', donvi_id=2)
        # thuoc6 = Thuoc(tenthuoc='Encorate', gia=4000, cachdung='1 lần sáng chiều', donvi_id=3)
        # db.session.add_all([thuoc1, thuoc2, thuoc3, thuoc4, thuoc5, thuoc6])
        # db.session.commit()

        # chitiet1 = ChiTietDonThuoc(soluong= 2, phieu_id=1, thuoc_id=1)
        # chitiet1_2 = ChiTietDonThuoc(soluong= 2, phieu_id=1, thuoc_id=2)
        # chitite1_3 = ChiTietDonThuoc(soluong= 2, phieu_id=1, thuoc_id=3)
        # db.session.add_all([chitiet1,chitiet1_2,chitite1_3])
        # db.session.commit()
