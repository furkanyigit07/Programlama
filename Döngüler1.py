baslangıc = int(input("Başlangıç sayısını giriniz: "))
bitis = int(input("Bitiş sayısını giriniz: "))
artış = int(input("Artış miktarını giriniz: "))
while baslangıc >= bitis:
    print("Başlangıç değeri bitiş değerinden küçük ve artış miktarı pozitif olmalıdır.")
    baslangıc = int(input("Başlangıç sayısını giriniz: "))
    bitis = int(input("Bitiş sayısını giriniz: "))
    artış = int(input("Artış miktarını giriniz: "))
if baslangıc < bitis:
    for i in range(baslangıc, bitis, artış):
        print(i)
else:
    print("Başlangıç değeri bitiş değerinden küçük ve artış miktarı pozitif olmalıdır.")