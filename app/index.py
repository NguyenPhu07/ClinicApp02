from flask import render_template, request
import dao
from app import app




@app.route("/")
def home():
    bacsi = dao.get_bacsi()
    stat = dao.count_quantity()
    return render_template("index.html", bacsis = bacsi, stats = stat)

@app.route("/register", methods=['get','post'])
def register_examination():
    ten = request.form.get('patientName')
    sodienthoai = request.form.get('phoneNumber')
    ngaysinh = request.form.get('dob')
    diachi = request.form.get('address')
    sex = request.form.get('gender')
    lydo = request.form.get('reason')
    if dao.add_patient_register(name=ten, phone=sodienthoai, gender=sex, date=ngaysinh, address=diachi, reason=lydo) == True:
        msg="Đăng Ký thành công"
    return render_template("index.html", message = msg)



@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)