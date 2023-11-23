# Terminal Commands
CLEAR = "\033[2J"   #-> Clear the screen
CLEAR_AND_RETURN = "\033[H"    #-> Clear the screen and gets the cursor to the top of the page

# Functions
def not_hesapla(line):
    """
    Bu fonksiyon öğrencilere ait verileri kullanarak, öğrencinin üç sınavdan almış
    aldığı notların ortalamasına karşılık gelen harfli not bilgisini hesaplar ve 
    kullanıcıya öğrenciyle ilgili yeni not bilgisini gösterir. 
    """

    line = line[:-1] # line = line.rstrip()
    info = line.split(":") 
    
    ogrenci_adi = info[0]             
    notlar = info[1].split(",")    

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "CB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DD"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "FD"
    else:
        harf = "FF"

    return ogrenci_adi + ": " + harf + "\n"


def ortalamalari_oku():
    """
    Bu fonksiyon sinav_notlari.txt içerisinde yer alan bilgileri okur ve
    öğrencilere ait ortalama bilgilerini öğrenci adı: ortalama şeklinde döndürür
    """
    with open("sinav_notlari.txt", mode="r", encoding="utf-8") as fhandle:
        for line in fhandle:
            print(not_hesapla(line), end="")
        

def not_gir():
    """
    Bu fonksiyon öğrenci ad, soyad, sınav bilgilerine ait girdileri alır ve
    bu bilgileri sinav_notlari.txt dosyası içerisine yazar
    """

    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    
    while True:
        not1 = input("İlk sınav: ")
        not2 = input("İkinci sınav: ")
        not3 = input("Üçüncü sınav: ")
        
        if not1.isdigit() and not2.isdigit() and not3.isdigit():
            break
        else:
            print("Lütfen geçerli not girdiğinizden emin olunuz.")

    with open("sinav_notlari.txt", mode="a", encoding="utf-8") as fhandle:
        student_info = f"{ad.capitalize()} {soyad.capitalize()}:{not1},{not2},{not3}\n"
        fhandle.write(student_info)
    


def notlari_kaydet():
    """
    Bu fonksiyon sinav_notlari.txt dosyası içerisine yazılan not bilgilerini okur ve
    sonuclar.txt dosyası içerisine ogrenci adı: not ortalaması şeklinde yazar
    """

    info_list = []
    
    with open("sinav_notlari.txt", mode="r", encoding="utf-8") as fhandle:
        for line in fhandle:
            info_list.append(not_hesapla(line))

    with open("sonuclar.txt", mode="w", encoding="utf-8") as fhandle_2:
        for info in info_list:
            fhandle_2.write(info)


# action to be taken
while True:
    # kullanıcıdan ona sunulan işlemlerden hangisini yapmak istediğini seç
    islem = input("\n1- Notları Oku\n2- Not Gir\n3- Notları Kaydet\n4- Çıkış\n\nYapmak İstediğiniz İşlemi Seçiniz: ")
    print(CLEAR, CLEAR_AND_RETURN)
    # seçimler için yapılacak işlemler
    if islem == "1":
        # tüm öğrencilerin ortalamasını oku
        ortalamalari_oku()
    elif islem == "2":
        # öğrenci için not bilgisi gir
        not_gir()
    elif islem == "3":
        # girilen not bilgilerini kaydet
        notlari_kaydet()
    elif islem == "4":
        # döngüyü sonlandır
        break
    else:
        print("Üzgünüz, istediğiniz işlemi gerçekleştiremiyoruz.\nLütfen geçerli bir işlem seçtiğinizden emin olunuz.")