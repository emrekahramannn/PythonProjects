# import module
import time


# create abstract data base w/ python dictionary
Erdal = {
    "Ad": "Erdal B*******",
    "Cinsiyet": True,
    "Şifre": "1881",
    "Hesap No": "979280008532",
    "Güncel Bakiye": 1500,
    "Ek Hesap": True,
    "Ek Hesap Bakiye": 500
}


Esin = {
    "Ad": "Esin G*******",
    "Cinsiyet": False,
    "Şifre": "1302",
    "Hesap No": "198798246723",
    "Güncel Bakiye": 7000,
    "Ek Hesap": False,
    "Ek Hesap Bakiye": 0
}


Emrullah = {
    "Ad": "Emrullah S*******",
    "Cinsiyet": True,
    "Şifre":"1478",
    "Hesap No": "5326046723",
    "Güncel Bakiye": 9000,
    "Ek Hesap": True,
    "Ek Hesap Bakiye": 4000
}


Emine = {
    "Ad": "Emine B*******",
    "Cinsiyet": False,
    "Şifre": "2516",
    "Hesap No": "25691678354",
    "Güncel Bakiye": 4500,
    "Ek Hesap": True,
    "Ek Hesap Bakiye": 1250
}


Ebuzer = {
    "Ad": "Ebuzer T****",
    "Cinsiyet": True,
    "Şifre": "6925",
    "Hesap No": "1247862452",
    "Güncel Bakiye": 4700,
    "Ek Hesap": False,
    "Ek Hesap Bakiye": 0
}



def bankaIslemleri(hesap):

    print("JEEZs".center(265))

    # Kullanıcıdan şifre bilgisini girmesini iste
    sifre = " "
    hak = 3
    
    while sifre != hesap["Şifre"]:
        print("Hesabınıza giriş yapmak için lütfen şifrenizi giriniz.")
        sifre = input("Şifre: ")
        hak -= 1
        
        if hak == 0:
            print("\nÜzgünüz art arda çok fazla yanlış denemede bulundunuz. ")
            quit()

    # Karşılama
    if hesap["Cinsiyet"]:
        print(f"\n{hesap['Ad'].split()[0].capitalize()} Bey, bankamıza hoşgeldiniz.\n")
    else:
        print(f"\n{hesap['Ad'].split()[0].capitalize()} Hanım, bankamıza hoşgeldiniz.\n")

    
    # kullanıcıdan yapacağı işlemi seçmesini iste
    islem = input("Yapmak istediğiniz işlemi seçiniz:\n1.Para Çekme\n2.Para Yatırma\n3.Ek Hesap İşlemleri\n")

    # Eğer para çekmek istiyorsa:
    if islem.lower() == "para çekme" or islem.lower() == "para cekme" or islem == "1":  #if islem in ["para çekme", "para cekme", "1"]
        paraCek(hesap)
    # Eğer para yatırmak istiyorsa:
    elif islem.lower() == "para yatırma" or islem.lower() == "para yatirma" or islem == "2": #if islem in ["para yatırma", "para yatirma", "2"]
        paraYatirma(hesap)
    # Eğer ek hesapla ilgili işlem yapmak istiyorsa:
    elif islem.lower() == "ek hesap işlemleri" or islem.lower() == "ek hesap islemleri" or islem == "3": #if islem in ["ek hesap işlemleri", "ek hesap islemleri", "3"]
        ekHesapislemleri(hesap)
    # Diğer:
    else:
        print("Üzgünüz, istediğiniz işlemi gerçekleştiremiyoruz.")

    print("JEEZs'i tercih ettiğiniz için teşekkür ederiz.".center(265))
    


def paraCek(hesap):
    # Karsılama
    print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, hoşgeldiniz.")

    # Hesaptan cekilecek miktarı belirle 
    while True:
        miktar = input("Lütfen hesabınızdan çekmek istediğiniz tutarı giriniz: ")
        try:
            miktar = int(miktar)
        except ValueError:
            print("Lütfen doğru tutar girdiğinizden emin olunuz.")
        else:
            break

    # Güncel bakiye girilen tutardan yüksekse parayı ver ve bakiyeyi güncelle
    if hesap["Güncel Bakiye"] >= miktar:
        print("İşlem Yapılıyor....")
        if miktar >= 5000:
            time.sleep(5)
        else:
            time.sleep(3)    
        print("Paranızı alabilirsiniz.")
        hesap["Güncel Bakiye"] -= miktar  # hesap["Güncel Bakiye"] = hesap["Güncel Bakiye"] - miktar
        bakiyeSorgula(hesap)
    
    # Güncel bakiye girilen tutardan düşükse: 
    else:
        # Kullanıcıya güncel bakiyesini bildir
        print(f"Sn. {hesap['Ad'].split()[1].capitalize()}, {hesap['Hesap No']} nolu hesabınıza ait güncel bakiyeniz {hesap['Güncel Bakiye']}tl.")
        
        # Kullanıcının ek hesabı varsa 
        if hesap["Ek Hesap"]:
            # Ek hesap ile işlem yapmak isteyip istemediğini sor
            ekHesapKullanimi = input("Para çekmek için ek hesabınızı kullanmak ister misiniz? (E/H) ")
            # Eğer ek hesapla işlem yapmak istiyorsa:
            if ekHesapKullanimi in ["e", "E", "evet", "Evet", "EVET"]:
                # Toplam bakiyeyi hesapla (güncel bakiye + ek hesap)
                toplamBakiye= hesap["Güncel Bakiye"] + hesap["Ek Hesap Bakiye"]
                
                # Eğer hesaba ait toplam bakiye çekilecek tutardan yüksekse kullanıcıya parasını ver
                if toplamBakiye >= miktar:
                    print("İşlem Yapılıyor....")
                    if miktar >= 5000:
                        time.sleep(5)
                    else:
                        time.sleep(3)    
                    print("Paranızı alabilirsiniz.")
                    # Güncel Bakiye ve Ek Hesapta kalan tutarı güncelle
                    hesap["Güncel Bakiye"] = 0                          # hesap["Güncel Bakiye"] = hesap["Güncel Bakiye"] - hesap["Güncel Bakiye"]   // hesap["Güncel Bakiye"] -= hesap["Güncel Bakiye"]
                    hesap["Ek Hesap Bakiye"] = toplamBakiye - miktar    # hesap["Ek Hesap Bakiye"] = hesap["Ek Hesap Bakiye"] - (miktar - hesap["Güncel Bakiye"])
                    bakiyeSorgula(hesap)
                
                # Toplam bakiye çekilecek miktardan az ise 
                else:
                    print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, {hesap['Hesap No']} nolu hesabınızda yeterli miktarda nakit yok.")
            
            # Eğer ek hesapla işlem yapmak istemiyorsa:
            else:
                print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, {hesap['Hesap No']} nolu hesabınızda yeterli miktar bulunmadığı için işlemi gerçekleştiremiyoruz.")

        else:
            print(f"Sn.{hesap['Ad'].split()[1].capitalize()} şuan için hesabınızda yeterli miktarda nakit bulunmadığından işlemi gerçekleştiremiyoruz.")



def paraYatirma(hesap):
    # Karsılamna
    print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, hoşgeldiniz.")

    # Hesaba yatırılacak miktarı belirle
    while True:
        miktar = input("Hesabınıza yatırmak istediğiniz tutarı giriniz: ")
        try:
            miktar = int(miktar)
        except ValueError:
            print("Lütfen geçerli bir tutar girdiğinizden emin olunuz.")
        else:
            break
    
    # print("Lütfen parayı alt kısımdaki bölüme yerleştiriniz")   --> ATM kullanımı için
    print("İşleminiz Yapılıyor, Lütfen Bekleyiniz...................")
    
    if miktar >= 5000:
        time.sleep(5)
    else:
        time.sleep(3)

    # Hesapta bulunan bakiyeyi güncelle
    hesap["Güncel Bakiye"] += miktar        #  hesap["Güncel Bakiye"] = hesap["Güncel Bakiye"] + miktar

    print("İşlem Tamamlandı.")
    bakiyeSorgula(hesap)



def ekHesapislemleri(hesap):
    
    # Kullanıcının ek hesabı varsa ek hesapta yapmak istediği işlemi seçmesini iste
    if hesap["Ek Hesap"]:
        print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, hoşgeldiniz.")

        islem = input("Yapmak istediğiniz işlemi seçiniz:\n1.Para yatırma\n2.Para çekme")

        if islem.lower() == "para yatırma" or islem.lower() == "para yatirma" or islem == "1":
            
            while True:
                miktar = input("Lütfen hesabınıza yatırmak istediğiniz tutarı giriniz: ")
                try:
                    miktar = int(miktar)
                except ValueError:
                    print("Lütfen doğru tutar girdiğinizden emin olunuz.")
                else:
                    break

            print("İşleminiz Yapılıyor, Lütfen Bekleyiniz...................")

            # Hesapta bulunan bakiyeyi güncelle
            hesap["Ek Hesap Bakiye"] += miktar

            print("İşlem Tamamlandı.")
            bakiyeSorgula(hesap)

        elif islem.lower() == "para çekme" or islem.lower() == "para cekme" or islem == "2":
            print(f"Güncel ek hesap bakiyeniz {hesap['Ek Hesap Bakiye']}tl")
            
            # Çekmek istediği tutarı kullanıcıdan iste
            while True:
                miktar = input("Lütfen hesabınıza yatırmak istediğiniz tutarı giriniz: ")
                try:
                    miktar = int(miktar)
                except ValueError:
                    print("Lütfen doğru tutar girdiğinizden emin olunuz.")
                else:
                    break

            if hesap["Ek Hesap Bakiye"] >= miktar:
                print("Lütfen bekleyiniz. İşleminiz devam ediyor..............")
                if miktar >= 1500:
                    time.sleep(4)
                else:
                    time.sleep(2)
                
                print("İşlem tamamlandı. Paranızı alabilirsiniz.")

                # Hesapta bulunan bakiyeyi güncelle
                hesap["Ek Hesap Bakiye"] -= miktar

                print(f"{hesap['Hesap No']} nolu ek hesabınızda kalan tutar {hesap['Ek Hesap Bakiye']}")

            else:
                print(f"Üzgünüz, {hesap['Hesap No']} nolu ek hesabınızda yeterli miktar bulunmuyor.")

        
    else:
        print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, {hesap['Hesap No']} nolu hesabınıza ait bir ek hesap bulunmuyor.")





def bakiyeSorgula(hesap):
    # karsıla ve Güncel Bakiye hakkında bilgi ver
    print(f"Sn.{hesap['Ad'].split()[1].capitalize()}, {hesap['Hesap No']} nolu hesabınızdaki güncel bakiyeniz {hesap['Güncel Bakiye']} tl.")
    
    # Kullanıcının ek hesabı varsa ek hesap hakkında bilgi ver
    if hesap["Ek Hesap"]:
        print(f"Ek hesabınızda bulunan tutar {hesap['Ek Hesap Bakiye']} tl.")



bankaIslemleri(Esin)