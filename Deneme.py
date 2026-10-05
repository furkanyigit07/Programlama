isimler = ["","","",""]
kullanıcı = input("kaç kişi eklemek istiyorsunuz: ")
for i in range(int(kullanıcı)):
    isim = input("isim giriniz: ")
    isimler[i] = isim
eklenen_isimler = [isim for isim in isimler if isim]
print("Eklenen isimler:", eklenen_isimler)
