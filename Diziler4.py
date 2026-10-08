# kullanıcılar dizisi oluşturuluyor oluşan dizi kullanıcı adı şifre ve email bilgilerini tutacak sözlük oluştur sözküğe en az bir veri girerek ekranda yazdırınız.
#tüm elemanları döngüyle ekrana yazdırınız.
kullanıcılar = [{"kullanıcı_adı": "furkan123", "şifre": "12345", "gmail": "yigitfurkan474@gmail.com"}, {"kullanıcı_adı": "yigit123", "şifre": "54321", "gmail": "yigitfurkan5234@gmail.com"}]
for kullanıcı in kullanıcılar:
    print("Kullanıcı Adı:", kullanıcı["kullanıcı_adı"])
    print("Şifre:", kullanıcı["şifre"])
    print("Gmail:", kullanıcı["gmail"])