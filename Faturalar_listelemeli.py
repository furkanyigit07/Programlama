#bir dizi başlangıcta boş olacak faturalar olucak su elektirik doğalgaz internet faturalartı kullanıcıya şuanki bütcesini sor faturaların hepsi bir sözlük içinde tutulcak en son fatura toplmı kullanıcı bütçesinden çıkan miktarı yazdıracak ve kullanıcıya kalan bütçesini gösterecek
faturalar = []
butce = float(input("Şuanki bütçenizi giriniz: "))
for i in range(4):
    Doğalgaz = float(input("Doğalgaz faturasının tutarını giriniz: "))
    Elektrik = float(input("Elektrik faturasının tutarını giriniz: "))
    Su = float(input("Su faturasının tutarını giriniz: "))
    İnternet = float(input("İnternet faturasının tutarını giriniz: "))
    faturalar.append({"ad": "Doğalgaz","tutar": Doğalgaz ,
                      "ad": "Elektrik","tutar": Elektrik ,
                      "ad": "Su","tutar": Su ,
                      "ad": "İnternet","tutar": İnternet 
                      })
    sonuc = butce - (Doğalgaz + Elektrik + Su + İnternet)
    print(f"Fatura toplamı: {Doğalgaz + Elektrik + Su + İnternet}")
    print(f"Kalan bütçe: {sonuc}")
    
