hak = 3
while hak > 0:
    kullanici_adi = input("kullanıcı adınızı giriniz: ")
    sifre = input("şifrenizi giriniz: ")
    if kullanici_adi == "test" and sifre == "123456789":
        print("Giriş başarılı")
        break
    else:
        hak -= 1
        print(f"Hatalı giriş yaptınız. Kalan hakkınız: {hak}")
        if hak == 0:
            print("Hakkınız kalmadı. Giriş yapamazsınız.")