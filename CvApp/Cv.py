import os
from types import resolve_bases
from flask import Flask, render_template, redirect, sessions, url_for, session, request, flash
from functools import wraps
import Forms
from werkzeug.utils import secure_filename
import Functions
import hashlib


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("Intrusion"))

    return decorated_function


def MaintenanceControl(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data =CvApp.SettingsSelect()
        control = data[3]
        if control == 0:
            return f(*args, **kwargs)
        else:
            return render_template("/Admin/Shared/Maintenance.html")

    return decorated_function


app = Flask(__name__, static_url_path='/static')
app.secret_key = "cvapp"
CvApp = Functions.CvApp()
app.config['UPLOAD_FOLDER'] = 'static/img'
UZANTILAR = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def uzanti_kontrol(dosyaadi):
    return '.' in dosyaadi and \
        dosyaadi.rsplit('.', 1)[1].lower() in UZANTILAR


@app.errorhandler(404)
def not_found(e):
  return render_template("/Admin/Shared/404.html"), 404

  
@app.route("/Nedmin/Maintenance/<string:id>")
@login_required
def Maintenance(id):
    control = CvApp.MaintenanceUpdate(id)
    if control == 2:
        flash("İşlem Başarısız...", "danger")
        return redirect(url_for("GeneralSettings"))
    else:
        flash("İşlem Başarılı...", "success")
        return redirect(url_for("GeneralSettings"))


@app.route("/")
@MaintenanceControl
def Index():
    general = CvApp.SettingsSelect()
    about = CvApp.AboutSelect()
    SocialMedia = CvApp.SocialMediaSelect()
    experince = CvApp.ExperienceList()
    education = CvApp.EducationList()
    ability = CvApp.AbilityList()
    return render_template("Index.html", about=about, SocialMedia=SocialMedia, experince=experince, education=education, ability=ability,set = general)


@app.route("/Nedmin/Intrusion")
def Intrusion():
    return render_template("/Admin/Shared/Intrusion.html")


@app.route("/Nedmin/Home")
@login_required
def AdminIndex():
    return render_template("/Admin/Index.html")


@app.route("/Nedmin/Logout")
@login_required
def AdminLogout():
    session.clear()
    return redirect(url_for("AdminLogin"))


@app.route("/Nedmin/Login", methods=["GET", "POST"])
def AdminLogin():
    login = Forms.LoginForm(request.form)
    if request.method == "POST" and login.validate():
        sifrele = hashlib.sha256()
        sifrele.update(login.password.data.encode("utf-8"))
        password = sifrele.hexdigest()
        loginControl = CvApp.LoginControl(
            login.email.data, password)
        if loginControl == 1:
            flash("E-Posta Bulunamadı...", "danger")
            return redirect(url_for("AdminLogin"))
        elif loginControl == 2:
            flash("Şifre Hatalı... :(", "danger")
            return redirect(url_for("AdminLogin"))
        elif loginControl == 3:
            session["logged_in"] = True
            session["email"] = login.email.data
            flash("Başarıyla Giriş Yaptınız...", "success")
            return redirect(url_for("AdminIndex"))
    else:
        return render_template("/Admin/Login.html", form=login)


@app.route("/Nedmin/About/Index", methods=["GET", "POST"])
@login_required
def AboutIndex():
    if request.method == "GET":
        data = CvApp.AboutSelect()
        if data == 1:
            flash("Hata Oluştu...", "danger")
            return redirect(url_for("AdminIndex"))
        else:
            form = Forms.AboutForm()
            form.aboutName.data = data[0]
            form.aboutSubname.data = data[1]
            form.aboutEmail.data = data[2]
            form.aboutTelephone.data = data[3]
            form.aboutAdress.data = data[6]
            form.aboutCountry.data = data[4]
            form.aboutCity.data = data[5]
            form.aboutDetails.data = data[8]
            photo= data[7]
            return render_template("/Admin/About/About.html", form=form, photo = photo)
    else:
        file = request.files['file']
        form = Forms.AboutForm(request.form)
        if file.filename == "":
            data = CvApp.AboutSelect()
            control = CvApp.AboutUpdate(form.aboutName.data, form.aboutSubname.data, form.aboutEmail.data, form.aboutTelephone.data,
                                        form.aboutCountry.data, form.aboutCity.data, form.aboutAdress.data, form.aboutDetails.data, data[7])
            if control == 1:
                flash("İşlem Başarısız...", "danger")
                return redirect(url_for("AboutIndex"))
            else:
                flash("İşlem Başarılı...", "success")
                return redirect(url_for("AboutIndex"))
        else:
            if file and uzanti_kontrol(file.filename):
                dosyaadi = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], dosyaadi))
                control = CvApp.AboutUpdate(form.aboutName.data, form.aboutSubname.data, form.aboutEmail.data, form.aboutTelephone.data,
                                            form.aboutCountry.data, form.aboutCity.data, form.aboutAdress.data, form.aboutDetails.data, dosyaadi)
                if control == 1:
                    flash("İşlem Başarısız...", "danger")
                    return redirect(url_for("AboutIndex"))
                else:
                    flash("İşlem Başarılı...", "success")
                    return redirect(url_for("AboutIndex"))
            else:
                flash("İzin Verilmeyen Dosya Uzantısı", "danger")
                return redirect(url_for("AdminIndex"))


@app.route("/Nedmin/About/SocialMedia", methods=["GET", "POST"])
@login_required
def SocialMedia():
    if request.method == "GET":
        data = CvApp.SocialMediaSelect()
        if data == 1:
            flash("Hata Oluştu...", "danger")
            return redirect(url_for("AdminIndex"))
        else:
            form = Forms.SoscialMediaForm()
            form.facebookLink.data = data[0]
            form.twitterLink.data = data[1]
            form.instagramLink.data = data[2]
            form.linkedinLink.data = data[3]
            form.githubLink.data = data[4]

            return render_template("/Admin/About/SocialMedia.html", form=form)
    else:
        form = Forms.SoscialMediaForm(request.form)
        control = CvApp.SocialMediaUpdate(form.facebookLink.data, form.twitterLink.data,
                                          form.instagramLink.data, form.linkedinLink.data, form.githubLink.data)
        if control == 1:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("SocialMedia"))
        else:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("SocialMedia"))


@app.route("/Nedmin/Ability/Index", methods=["GET", "POST"])
@login_required
def Ability():
    form = Forms.AbilityForm(request.form)
    if request.method == "POST" and form.validate():
        control = CvApp.AbilityAdd(form.abilityValue.data)
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("Ability"))
        else:
            flash("İşlem Başarısız...", "danger")
        return redirect(url_for("Ability"))
    else:
        controlData = CvApp.AbilityList()
        return render_template("/Admin/Ability/Index.html", form=form, data=controlData)


@app.route("/Nedmin/Ability/Delete/<string:id>")
@login_required
def AbilityDelete(id):
    control = CvApp.AbilityDelete(id)
    if control == 1:
        flash("İşlem Başarılı...", "success")
        return redirect(url_for("AdminIndex"))
    else:
        flash("İşlem Hatalı...", "danger")
        return redirect(url_for("AdminIndex"))


@app.route("/Nedmin/General/Settings", methods=["GET", "POST"])
@login_required
def GeneralSettings():
    if request.method == "GET":
        data = CvApp.SettingsSelect()
        if data == 1:
            flash("Hata Oluştu...", "danger")
            return redirect(url_for("AdminIndex"))
        else:
            form = Forms.GeneralSettingsForm()
            form.siteTitle.data = data[0]
            form.siteSubTitle.data = data[1]
            form.siteKeyword.data = data[2]
            bakim=data[3]
            print(bakim)
            return render_template("/Admin/General/Settings.html", form=form,bakim = bakim)
    else:
        form = Forms.GeneralSettingsForm(request.form)
        control = CvApp.SettingsUpdate(form.siteTitle.data, form.siteSubTitle.data, form.siteKeyword.data)
        if control == 1:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("GeneralSettings"))
        else:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("GeneralSettings"))


@app.route("/Nedmin/Education/Add", methods=["GET", "POST"])
@login_required
def EducationAdd():
    form = Forms.EducationForm(request.form)
    if request.method == "POST" and form.validate():
        control = CvApp.EducationAdd(form.educationTitle.data, form.educationSubTitle.data, form.educationDetail.data,
                                     request.form["start"], request.form["end"])
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("EducationAdd"))
        else:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("EducationAdd"))
    else:
        return render_template("/Admin/Education/Add.html", form=form)


@app.route("/Nedmin/Education/Delete/<string:id>")
@login_required
def EducationDelete(id):
    control = CvApp.EducationDelete(id)
    if control == 1:
        flash("İşlem Başarılı...", "success")
        return redirect(url_for("AdminIndex"))
    else:
        flash("İşlem Hatalı...", "danger")
        return redirect(url_for("AdminIndex"))


@app.route("/Nedmin/Education/Update/<string:id>", methods=["GET", "POST"])
@login_required
def EducationUpdate(id):
    if request.method == "GET":
        control = CvApp.EducationSelect(id)
        if control == 0:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("EducationList"))
        else:
            education = control
            form = Forms.EducationForm()
            form.educationTitle.data = education[1]
            form.educationSubTitle.data = education[2]
            form.educationDetail.data = education[3]
            start = education[4]
            end = education[5]
            return render_template("/Admin/Education/Update.html", form=form, start=start, end=end)
    else:
        form = Forms.EducationForm(request.form)
        control = CvApp.EducationUpdate(form.educationTitle.data, form.educationSubTitle.data,
                                        form.educationDetail.data, request.form["start"], request.form["end"], id)
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("EducationList"))
        else:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("EducationList"))


@app.route("/Nedmin/Education/List")
@login_required
def EducationList():
    controlData = CvApp.EducationList()
    return render_template("/Admin/Education/List.html", data=controlData)


@app.route("/Nedmin/Experience/Add", methods=["GET", "POST"])
@login_required
def ExperienceAdd():
    form = Forms.ExperienceForm(request.form)
    if request.method == "POST" and form.validate():
        control = CvApp.ExperienceAdd(form.experienceTitle.data, form.experienceSubTitle.data,
                                      form.experienceDetail.data, request.form["start"], request.form["end"])
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("ExperienceAdd"))
        else:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("ExperienceAdd"))
    else:
        return render_template("/Admin/Experience/Add.html", form=form)


@app.route("/Nedmin/Experience/Update/<string:id>", methods=["GET", "POST"])
@login_required
def ExperienceUpdate(id):
    if request.method == "GET":
        control = CvApp.ExperienceSelect(id)
        if control == 0:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("ExperienceList"))
        else:
            experience = control
            form = Forms.ExperienceForm()
            form.experienceTitle.data = experience[1]
            form.experienceSubTitle.data = experience[2]
            form.experienceDetail.data = experience[3]
            start = experience[4]
            end = experience[5]
            return render_template("/Admin/Experience/Update.html", form=form, start=start, end=end)
    else:
        form = Forms.ExperienceForm(request.form)
        control = CvApp.ExperienceUpdate(form.experienceTitle.data, form.experienceSubTitle.data,
                                         form.experienceDetail.data, request.form["start"], request.form["end"], id)
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("ExperienceList"))
        else:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("ExperienceList"))


@app.route("/Nedmin/Experience/Delete/<string:id>")
@login_required
def ExperienceDelete(id):
    control = CvApp.ExperienceDelete(id)
    if control == 1:
        flash("İşlem Başarılı...", "success")
        return redirect(url_for("AdminIndex"))
    else:
        flash("İşlem Hatalı...", "danger")
        return redirect(url_for("AdminIndex"))


@app.route("/Nedmin/Experience/List")
@login_required
def ExperienceList():
    controlData = CvApp.ExperienceList()
    return render_template("/Admin/Experience/List.html", data=controlData)


@app.route("/Nedmin/Users/Index", methods=["GET", "POST"])
@login_required
def UserAdd():
    form = Forms.UsersForm(request.form)
    controlData = CvApp.UserList()
    if request.method == "POST" and form.validate():
        sifrele = hashlib.sha256()
        sifrele.update(form.password.data.encode("utf-8"))
        password = sifrele.hexdigest()
        userControl = CvApp.UserAdd(
            form.name.data, form.email.data, password)
        if userControl == 1:
            flash("işlem Başarılı...", "success")
            return redirect(url_for("UserAdd"))
        else:
            flash("işlem Başarısız...", "danger")
            return redirect(url_for("UserAdd"))
    else:
        return render_template("/Admin/Users/Index.html", form=form, data=controlData)


@app.route("/Nedmin/Users/Update/<string:id>", methods=["GET", "POST"])
@login_required
def UsersUpdate(id):
    if request.method == "GET":
        control = CvApp.UserSelect(id)
        if control == 0:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("UserAdd"))
        else:
            user = control
            email = control[2]
            form = Forms.UsersForm()
            form.name.data = user[1]
            return render_template("/Admin/Users/Update.html", form=form, email=email)
    else:
        form = Forms.UsersForm(request.form)
        sifrele = hashlib.sha256()
        sifrele.update(form.password.data.encode("utf-8"))
        password = sifrele.hexdigest()
        oldsifre= hashlib.sha256()
        oldsifre.update(request.form["oldpassword"].encode("utf-8"))
        oldpassword = oldsifre.hexdigest()
        control = CvApp.UserUpdate(
            oldpassword, form.name.data, password, id)
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("UserAdd"))
        elif control == 2:
            flash("Mevcut Parola Hatalı...", "danger")
            return redirect(url_for("UserAdd"))
        else:
            flash("İşlem Başarısız...", "danger")
            return redirect(url_for("UserAdd"))


@app.route("/Nedmin/Users/Delete/<string:id>")
@login_required
def UsersDelete(id):
    email = session["email"]
    data = CvApp.UserSelectEmail(str(email))
    dataid=data[0]
    if dataid != id:
        flash("Giriş Yaptığınız Hesabı Silemezsiniz !", "danger")
        return redirect(url_for("AdminIndex"))
    else:
        control = CvApp.UserDelete(id)
        if control == 1:
            flash("İşlem Başarılı...", "success")
            return redirect(url_for("AdminIndex"))
        else:
            flash("İşlem Hatalı...", "danger")
            return redirect(url_for("AdminIndex"))


if __name__ == "__main__":
    app.run(debug=True)
