fatura={
    "Doğalgaz": 
    {
    "abone_no": 123,
    "tutar": 500
    },
    "Elektrik":
    {
    "abone_no": 1234,
    "tutar": 300
    },
    "Su":
    {
    "abone_no": 12345,
    "tutar": 200
    },
    "İnternet": 
    {
    "abone_no": 123456,
    "tutar": 100
    }      
}
for i in fatura:
    print(f"{i} faturası tutarı: {fatura[i]['tutar']}")

#kullanıcıya kaç sayı girmesini sor sayılar adında bir tane dizi kullanıcıdının girdiği sayıları bu dizide tutularak yazdırılacak