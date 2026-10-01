G_sayi = int(input("Bir sayi giriniz: "))
İndirim = 10
büyük_indirim = 20
Yüzde = 100
if G_sayi > 1000:
    indirimli_fiyat = G_sayi - (G_sayi * büyük_indirim / Yüzde)
    print(f"İndirimli fiyat: {indirimli_fiyat}")
elif G_sayi > 500:
    indirimli_fiyat = G_sayi - (G_sayi * İndirim / Yüzde)
    print(f"İndirimli fiyat: {indirimli_fiyat}")
else:
    print("İndirim uygulanamaz")


