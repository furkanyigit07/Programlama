sabit_fatura_numarasi = "frkn123456"
sabit_hesap_numarasi = "1234567890"
fatura_tutari = 1500
while True:
    kullanici_fatura_numarasi = input("Fatura numarasını girin: ")
    if kullanici_fatura_numarasi == sabit_fatura_numarasi:
        break
    print("Fatura numarası hatalı. Lütfen tekrar deneyin.")
while True:
    kullanici_hesap_numarasi = input("Ödeme yapılacak hesap numarasını girin: ")
    if kullanici_hesap_numarasi == sabit_hesap_numarasi:
        break
    print("Hesap numarası hatalı. Lütfen tekrar deneyin.")
while True:
    odeme_tutari = float(input("Ödemek istediğiniz tutarı girin: "))
    if odeme_tutari == fatura_tutari:
        print("Ödeme tamamlandı.")
        break
    print("Fatura tutarı 1500 TL'dir. Lütfen doğru tutarı girin.")