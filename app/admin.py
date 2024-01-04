from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app.models import BacSi, BenhNhan, DKKham, DSCaKham, PhieuKhamBenh, Thuoc, DonVi, DanhMuc, ChiTietDonThuoc, UserRoleEnum
from app import app, db
from flask_login import logout_user, current_user
from sqlalchemy import func, Integer
from flask import redirect, request, render_template
import dao


admin = Admin(app=app, name='Quản lý phòng mạch', template_mode='bootstrap4')

class AuthicateLogout(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class AuthticatedAdminModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthicatedAdminBase(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthticatedNurseModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.NURSE

class AuthticatedDoctorModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.DOCTOR

class AuthticatedCashierModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.CASHIER



class AuthicatedAdminBase(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN



#--------view-admin-----------------------------------------
class MyDrugView(AuthticatedAdminModel):
    column_list = ['id', 'tenthuoc', 'gia', 'cachdung']
    can_export = True
    edit_modal = True
    can_view_details = True
    details_modal = True
    form_excluded_columns = ['DSPhieuKham', 'DSDanhmuc']
    column_searchable_list = ['tenthuoc']


class MyDVView(AuthticatedAdminModel):
    column_list = ['loaidonvi', 'DSThuoc']
    can_create = False

class MyStasView(AuthicatedAdminBase):
    @expose("/")
    def index(self):
        stat = dao.count_quantity()
        return self.render('admin/stats.html', stats=stat)


class MyListExamination(ModelView):
    can_delete = False
    can_export = True
    edit_modal = True
    can_view_details = True
    details_modal = True

class MyClinicForm(ModelView):
    form_excluded_columns = ['DSHoaDon', 'DSThuoc']



class MyLogoutView(AuthicateLogout):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


class MyCreateView(ModelView):
   pass


admin.add_view(MyDVView(DonVi, db.session))
admin.add_view(MyDrugView(Thuoc, db.session))
admin.add_view(MyStasView(name='Thống kê báo cáo'))
admin.add_view(MyListExamination(DSCaKham, db.session))
admin.add_view(MyClinicForm(PhieuKhamBenh, db.session))
admin.add_view(ModelView(ChiTietDonThuoc, db.session))
admin.add_view(MyLogoutView(name='Đăng xuất'))











