    # >>> Talaba haqida malumotlar

class Talaba:
    """Talaba nomli class yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning hususuyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_age(self,yil):
        """Talabaning tugilgan yilini qaytaradi"""
        return yil - self.tyil

    def get_lastname(self):
        """Talaba familiyasini qaytaradi"""
        return self.familiya

    def get_info(self):
        """Talaba haqida umumiy malumot"""
        return f"ismi {self.ism}, familiyasi {self.familiya}, yili {self.tyil} yil, {self.bosqich} - bosqichda"

    def set_yangi_bosqich(self,yangi_bosqich):
        """Talabanig kursini yangilaydi"""
        self.bosqich = yangi_bosqich


talaba1 = Talaba("Dilshodbek","Yoqubov",2002)
talaba2 = Talaba("Jamshidbek","Ergashev",1992)
# print(talaba1.get_name())
print(talaba1.get_info())


    # >>> User haqida malumotlar

class User:
    """User classi"""
    def __init__(self,ism,familiya,gmail,parol):
        """User haqida malumotlar"""
        self.ism = ism
        self.familiya = familiya
        self.gmail = gmail
        self.parol = parol


    def get_info(self):
        """Foydalanuvchi haqida umumiy malumotlar"""
        return f"Ism = {self.ism}, Familiya = {self.familiya}, Gmail = {self.gmail}, Parol = {self.parol}"

    def get_fullname(self):
        """Foydalanuvchi ismi va familiyasini qaytaradi"""
        return f"Ismi {self.ism}, Familiyasi {self.familiya}"

    def get_gmail(self):
        """User gmailni qaytaradi"""
        return self.gmail

    def get_password(self):
        """User gmail password"""
        return self.parol


foydalanuvchi = User("Dilshodbek","Yoqubov","backenddevvv@gmail.com",12345678)
foydalanuvchi1 = User("Jamshidbek","Ergashev","jamshid@gmail.com",21214343)
foydalanuvchi2 = User("Diyorbek","Adhamov","diyorjon@gmail.com",123321)
print(foydalanuvchi.get_info())
# print(foydalanuvchi2.get_password())


    # >>> Avtolar haqida malumotlar

class Avto:
    """Avto classi"""
    def __init__(self, model, karopka, yili, narx):
        """Avto hususiyatlari"""
        self.model = model
        self.karopka = karopka
        self.yili = yili
        self.narx = narx
        self.km = 0

    def get_info(self):
        """Avto haqida toliq malumot"""
        return f"Modeli {self.model}, Karopkasi {self.karopka}, Yili {self.yili}, Narxi {self.narx}, Kilometr {self.km}"

    def get_fullname(self):
        """Avtoni model, yili, kilometrni qaytaradi"""
        return f"Modeli {self.model}, Yili {self.yili}, Km {self.km}"

    def update_km(self, kmson):
        """Km yangilab boradi"""
        return self.km

avto1 = Avto("Cobalt","Mexanik",2020, 10000)
avto2 = Avto("Spark","Avtomat",2018, 8000)
print(avto1.get_info())
# print(avto1.update_km(1000))
# print(avto2.get_fullname())


    # >>> AvtoSalon manzili va bor avtolar haqida malumotlar

class Avtosalon:
    """Avtosalon classi"""
    def __init__(self, salon_nomi, manzili, bor_avtolar):
        """Avtosalon hususiyatlari"""
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.bor_avtolar = bor_avtolar

    def get_info(self):
        """Salonni umumiy malumotlari"""
        return f"Salon:'{self.salon_nomi}', Manzili: {self.manzili}, {self.bor_avtolar}"

avtosalon = Avtosalon("777 SERVICES", "Marhamat tumani, 'Saroy' to'yxonasi yonida","Avtolarimiz: Cobalt, Spark, Nexia3, Malibu")
avtosalon1 = Avtosalon("STARK CERVIES","Andijon sh, Holis savdo-majmuasi yonida"," KIA, TOYOTA, RAVON  shu modeldagi avtomobillar bor")

print(avtosalon1.get_info())
print(avtosalon.get_info())




