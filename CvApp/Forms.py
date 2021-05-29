from wtforms import Form, StringField, TextAreaField, PasswordField, validators,TextAreaField

class UsersForm(Form):
    email=StringField("E-Posta: ", validators=[validators.Email(message="Lütfen Geçerli Bir E-Posta Adresi Giriniz !")])
    name = StringField("İsim Soyisim", validators=[validators.Length(min=5, max=200, message="Ad ve Soyad 5 Karakterden Kısa Olamaz")])
    password = PasswordField("Parola:", validators=[
        validators.DataRequired(message="Lütfen Bir Parola Belirleyin"),
        validators.EqualTo(fieldname="confirm", message="Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField("Tekrar Parola")

class LoginForm(Form):
    email=StringField("E-Posta: ", validators=[validators.Email(message="Lütfen Geçerli Bir E-Posta Adresi Giriniz !")])
    password = PasswordField("Parola:", validators=[validators.DataRequired(message="Lütfen Bir Parola Belirleyin")])

class EducationForm(Form):
    educationTitle = StringField("Başlık", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    educationSubTitle = StringField("Alt Başlık", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    educationDetail = TextAreaField("Detay", validators=[validators.Length(max=500,message="Maksimum 500 Karakter"),
        validators.DataRequired(message="Lütfen Bu Alanı Doldurunuz")])

class AbilityForm(Form):
    abilityValue = StringField("Yetenek", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])

class ExperienceForm(Form):
    experienceTitle = StringField("Başlık", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    experienceSubTitle = StringField("Alt Başlık", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    experienceDetail = TextAreaField(" Detay", validators=[validators.Length(max=500,message="Maksimum 500 Karakter"),
        validators.DataRequired(message="Lütfen Bu Alanı Doldurunuz")])

class SoscialMediaForm(Form):
    facebookLink = StringField("Facebook", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    twitterLink = StringField("Twitter", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    instagramLink = StringField("Instagram", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    linkedinLink = StringField("Linkedin", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    githubLink = StringField("Github", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])

class GeneralSettingsForm(Form):
    siteTitle = StringField("Site Başlık", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    siteSubTitle = StringField("Site Açıklama", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    siteKeyword = StringField("Site Anahtar Kelime", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])

class AboutForm(Form):
    aboutName = StringField("Ad", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutSubname = StringField("Soyad", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutEmail = StringField("E-Posta", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutTelephone = StringField("Telefon", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutCountry = StringField("Ülke", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutCity = StringField("Şehir", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutAdress = StringField("Adres", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])
    aboutDetails = TextAreaField("Detay", validators=[validators.DataRequired(message="Lütfem Bu Alanı Doldurunuz")])