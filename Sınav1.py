name = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli", "Zeynep", "Elif", "Murat", "Hüseyin"]
print("Yapabileceğiniz işlemler: 1. İsim ekleme 2. İsim arama")
neseye_yapmak_istediginizi_sec = input("Lütfen yapmak istediğiniz işlemi seçiniz (1 veya 2): ")
if neseye_yapmak_istediginizi_sec == "1":
    isim_ekle = input("Lütfen eklemek istediğiniz ismi giriniz: ")
    if isim_ekle not in name:
        name.append(isim_ekle)
        print(f"{isim_ekle} listeye eklendi.")
    else:
        print(f"{isim_ekle} zaten listede mevcut.")
elif neseye_yapmak_istediginizi_sec == "2":
    isim_ara = input("Lütfen aramak istediğiniz ismi giriniz: ")
    if isim_ara in name:
        print(f"{isim_ara} listede bulundu.")
    else:
        print(f"{isim_ara} listede bulunamadı.")

