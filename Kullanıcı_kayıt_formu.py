#Bir kullanıcı kayıt formu oluşacak formda kullanıcı adı Şifre Şifre Tekrarı mail ve telefon numarısı sormaktadır kullanıcıların girmiş olduğu verileri sözluk oluşturarak tutunuz tüm kullanıcıları bir dizide toplayınız Kaç kullanıcı kaydı olacağını kullanıcıya sor
kullanıcı_listesi=[]
girilecek_sayi=int(input("Kaç kullanıcı kaydı yapılacak? :"))
for i in range(girilecek_sayi):
    kullanıcı_adı=input("Kullanıcı adını giriniz: ")
    şifre=input("Şifreyi giriniz: ")
    şifre_tekrar=input("Şifreyi tekrar giriniz: ")
    mail=input("Mail adresinizi giriniz: ")
    telefon_numarası=input("Telefon numaranızı giriniz: ")

    kullanıcı_bilgileri={
        "Kullanıcı Adı": kullanıcı_adı,
        "Şifre": şifre,
        "Şifre Tekrar": şifre_tekrar,
        "Mail": mail,
        "Telefon Numarası": telefon_numarası
    }

    kullanıcı_listesi.append(kullanıcı_bilgileri)
