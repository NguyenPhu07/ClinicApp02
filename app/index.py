from flask import render_template, request, redirect, jsonify, url_for
import dao
from app import app, login
from flask_login import login_user
from flask_admin import Admin, BaseView, expose, AdminIndexView



@app.route("/")
def home():
    bacsi = dao.get_bacsi()
    return render_template("index.html", bacsis = bacsi)


@app.route("/register", methods=['post'])
def register_examination():
    ten = request.form.get('patientName')
    sodienthoai = request.form.get('phoneNumber')
    ngaysinh = request.form.get('dob')
    diachi = request.form.get('address')
    sex = request.form.get('gender')
    lydo = request.form.get('reason')

    if dao.test_patient(ten) == True:
        msg=" Bạn đã Đăng Ký trước đó "
    else:
        if dao.add_patient_register(name=ten, phone=sodienthoai, gender=sex, date=ngaysinh, address=diachi,reason=lydo) == True:
            msg = "Đăng Ký thành công"
    return render_template("index.html", message = msg)

@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username,password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route('/admin1')
def admin1():
    return redirect('/admin')








@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)






if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
