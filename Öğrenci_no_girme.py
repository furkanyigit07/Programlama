Ogrenci_no = input("kaç öğrencinin numarasını girmek istiyorsunuz: ")
Ogrenci_no_ort = int(Ogrenci_no) // 2
ogrenci_numaralari = []
for i in range(int(Ogrenci_no)):
    numara = input("Öğrenci numarasını giriniz: ")
    ogrenci_numaralari.append(numara)
print("Eklenen öğrenci numaraları:", ogrenci_numaralari)
if len(ogrenci_numaralari) > 0:
    ortalama = sum(int(numara) for numara in ogrenci_numaralari) / len(ogrenci_numaralari)
    print("Öğrenci numaralarının ortalaması:", ortalama)