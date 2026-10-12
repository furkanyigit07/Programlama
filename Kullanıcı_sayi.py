#kullanıcıya kaç sayı girmesini sor sayılar adında bir tane dizi kullanıcıdının girdiği sayıları bu dizide tutularak yazdırılacak
sayilar = []
sayi_adedi = int(input("Kaç sayı gireceksiniz? "))
for i in range(sayi_adedi):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(sayi)
print("Girilen sayılar:")
for sayi in sayilar:  
    print(sayi)
