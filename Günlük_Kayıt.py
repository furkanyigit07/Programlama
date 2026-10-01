T_Kayıt = 47
Günlük_sayfa_kayıt = 10
Sayfa_sayısı = T_Kayıt // Günlük_sayfa_kayıt
if T_Kayıt % Günlük_sayfa_kayıt != 0:
    Sayfa_sayısı += 1
print(f"Toplam sayfa sayısı: {Sayfa_sayısı}")
son_sayfa_kayıt = T_Kayıt % Günlük_sayfa_kayıt
if son_sayfa_kayıt == 0:
    son_sayfa_kayıt = Günlük_sayfa_kayıt
print(f"Son sayfada gösterilecek kayıt sayısı: {son_sayfa_kayıt}")