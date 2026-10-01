sayı = 50
hak = 10
while hak > 0:
    tahmin = int(input("Bir sayı tahmin edin (1-100): "))
    if tahmin == sayı:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break
    if tahmin < sayı:
        hak -= 1
        print(f"Daha büyük bir sayı tahmin edin.{hak} hakkınız kaldı.")
    elif tahmin > sayı:
        hak -= 1
        print(f"Daha küçük bir sayı tahmin edin.{hak} hakkınız kaldı.")