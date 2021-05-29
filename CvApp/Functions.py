import pymysql


class CvApp():

    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1', user='root', passwd='', db='cvapp')

    def MaintenanceUpdate(self,maintenance):
        try:
            cursor = self.conn.cursor()
            query = "Update ayarlar Set ayar_bakim=%s"
            cursor.execute(query, (maintenance))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            return 2

    def SettingsSelect(self):
        try:
            cursor = self.conn.cursor()
            query = "Select * From ayarlar"
            cursor.execute(query)
            data = cursor.fetchone()
            return data
        except:
            return 1

    def AboutSelect(self):
        try:
            cursor = self.conn.cursor()
            query = "Select * From hakkinda"
            cursor.execute(query)
            data = cursor.fetchone()
            return data
        except:
            return 1

    def AboutUpdate(self, name, firstname, email, tel, country, city, adress, details, photo):
        try:
            cursor = self.conn.cursor()
            query = "Update hakkinda Set hakkinda_ad=%s, hakkinda_soyad=%s, hakkinda_eposta=%s, hakkinda_telefon=%s, hakkinda_ulke=%s,hakkinda_sehir=%s, hakkinda_adres=%s, hakkinda_detay=%s, hakkinda_resim=%s"
            cursor.execute(query, (name, firstname, email, tel,
                           country, city, adress, details, photo))
            self.conn.commit()
            cursor.close()
            return 2
        except:
            return 1

    def SettingsUpdate(self, title, subtitle, keyword):
        try:
            cursor = self.conn.cursor()
            query = "Update ayarlar Set ayar_baslik=%s, ayar_altbaslik=%s, ayar_anahtar=%s"
            cursor.execute(query, (title, subtitle, keyword))
            self.conn.commit()
            cursor.close()
            return 2
        except:
            return 1

    def SocialMediaSelect(self):
        try:
            cursor = self.conn.cursor()
            query = "Select * From sosyalmedya"
            cursor.execute(query)
            data = cursor.fetchone()
            return data
        except:
            return 1

    def SocialMediaUpdate(self, facebook, twitter, instagram, linkedin, github):
        try:
            cursor = self.conn.cursor()
            query = "Update sosyalmedya Set sosyal_facebook=%s, sosyal_twitter=%s, sosyal_instagram=%s, sosyal_linkedin=%s, sosyal_github=%s"
            cursor.execute(query, (facebook, twitter,instagram, linkedin, github))
            self.conn.commit()
            cursor.close()
            return 2
        except:
            return 1

    def UserAdd(self, name, email, password):
        try:
            cursor = self.conn.cursor()
            query = "Insert into admin(admin_adsoyad, admin_eposta, admin_password) VALUES(%s,%s,%s)"
            cursor.execute(query, (name, email, password))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            cursor.close()
            return 2

    def UserUpdate(self, oldpassword, name, password, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from admin where admin_id = %s and admin_password= %s"
            result = cursor.execute(query, (id, oldpassword))
            if result > 0:
                query = "Update admin Set admin_adsoyad = %s, admin_password=%s where admin_id = %s"
                cursor.execute(query, (name, password, id))
                self.conn.commit()
                cursor.close()
                return 1
            else:
                cursor.close()
                return 2
        except:
            cursor.close()
            return 3

    def UserDelete(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from admin where admin_id = %s"
            result = cursor.execute(query, (id,))
            if result > 0:
                query2 = "Delete from admin where admin_id = %s"
                cursor.execute(query2, (id,))
                self.conn.commit()
                cursor.close()
                return 1
            else:
                cursor.close()
                return 2
        except:
            return 3

    def UserSelect(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from admin where admin_id = %s"
            result = cursor.execute(query, (id,))
            if result == 0:
                return 0
            else:
                user = cursor.fetchone()
                return user
        except:
            return 0

    def UserSelectEmail(self,email):
        try:
            cursor = self.conn.cursor()
            query = "Select * from admin where admin_eposta = %s"
            result = cursor.execute(query, (email,))
            if result == 0:
                return 0
            else:
                user = cursor.fetchone()
                return user
        except:
            return 0

    def UserList(self):
        cursor = self.conn.cursor()
        query = "Select * From admin"
        result = cursor.execute(query)
        if result > 0:
            data = cursor.fetchall()
            return data
        else:
            cursor.close()
            return 1

    def LoginControl(self, email, password):
        cursor = self.conn.cursor()
        query = "SELECT * FROM admin WHERE admin_eposta=%s "
        result = cursor.execute(query, (email,))
        if result > 0:
            data = cursor.fetchone()
            real_password = data[3]
            if real_password == password:
                cursor.close()
                return 3
            else:
                cursor.close()
                return 2
        else:
            cursor.close()
            return 1

    def AbilityAdd(self, abilityname):
        try:
            cursor = self.conn.cursor()
            query = "Insert into yetenekler(yetenek_ad) VALUES(%s)"
            cursor.execute(query, (abilityname))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            cursor.close()
            return 2

    def AbilityDelete(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from yetenekler where yetenek_id = %s"
            result = cursor.execute(query, (id,))
            if result > 0:
                query2 = "Delete from yetenekler where yetenek_id = %s"
                cursor.execute(query2, (id,))
                self.conn.commit()
                cursor.close()
                return 1
            else:
                cursor.close()
                return 2
        except:
            return 3

    def AbilityList(self):
        cursor = self.conn.cursor()
        query = "Select * From yetenekler"
        result = cursor.execute(query)
        if result > 0:
            data = cursor.fetchall()
            return data
        else:
            cursor.close()
            return 1

    def EducationAdd(self, title, subtitle, detail, start, end):
        try:
            cursor = self.conn.cursor()
            query = "Insert into egitimler(egitim_baslik, egitim_altbaslik ,egitim_detay, egitim_baslangic, egitim_bitis) VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(query, (title, subtitle, detail, start, end))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            cursor.close()
            return 2

    def EducationSelect(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from egitimler where egitim_id = %s"
            result = cursor.execute(query, (id,))
            if result == 0:
                return 0
            else:
                education = cursor.fetchone()
                return education
        except:
            return 0

    def EducationUpdate(self, title, subtitle, detail, start, end, id):
        try:
            cursor = self.conn.cursor()
            query = "Update egitimler Set egitim_baslik = %s, egitim_altbaslik=%s, egitim_detay=%s, egitim_baslangic=%s, egitim_bitis=%s where egitim_id = %s"
            cursor.execute(query, (title, subtitle, detail, start, end, id))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            return 2

    def EducationDelete(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from egitimler where egitim_id = %s"
            result = cursor.execute(query, (id,))
            if result > 0:
                query2 = "Delete from egitimler where egitim_id = %s"
                cursor.execute(query2, (id,))
                self.conn.commit()
                cursor.close()
                return 1
            else:
                cursor.close()
                return 2
        except:
            return 3

    def EducationList(self):
        cursor = self.conn.cursor()
        query = "Select * From egitimler"
        result = cursor.execute(query)
        if result > 0:
            data = cursor.fetchall()
            return data
        else:
            cursor.close()
            return 1

    def ExperienceAdd(self, title, subtitle, detail, start, end):
        try:
            cursor = self.conn.cursor()
            query = "Insert into deneyimler(deneyim_baslik, deneyim_altbaslik ,deneyim_detay, deneyim_baslangic, deneyim_bitis) VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(query, (title, subtitle, detail, start, end))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            cursor.close()
            return 2

    def ExperienceSelect(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from deneyimler where deneyim_id = %s"
            result = cursor.execute(query, (id,))
            if result == 0:
                return 0
            else:
                experience = cursor.fetchone()
                return experience
        except:
            return 0

    def ExperienceUpdate(self, title, subtitle, detail, start, end, id):
        try:
            cursor = self.conn.cursor()
            query = "Update deneyimler Set deneyim_baslik = %s, deneyim_altbaslik=%s, deneyim_detay=%s, deneyim_baslangic=%s, deneyim_bitis=%s where deneyim_id  = %s"
            cursor.execute(query, (title, subtitle, detail, start, end, id))
            self.conn.commit()
            cursor.close()
            return 1
        except:
            return 2

    def ExperienceDelete(self, id):
        try:
            cursor = self.conn.cursor()
            query = "Select * from deneyimler where deneyim_id = %s"
            result = cursor.execute(query, (id,))
            if result > 0:
                query2 = "Delete from deneyimler where deneyim_id = %s"
                cursor.execute(query2, (id,))
                self.conn.commit()
                cursor.close()
                return 1
            else:
                cursor.close()
                return 2
        except:
            return 3

    def ExperienceList(self):
        cursor = self.conn.cursor()
        query = "Select * From deneyimler"
        result = cursor.execute(query)
        if result > 0:
            data = cursor.fetchall()
            return data
        else:
            cursor.close()
            return 1
