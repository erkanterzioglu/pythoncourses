def topla(sayi1,sayi2):
    return sayi1+sayi2


def cikar(sayi1,sayi2):
    return sayi1-sayi2


def bol(sayi1,sayi2):
    return sayi1/sayi2


def carp(sayi1,sayi2):
    return sayi1*sayi2


print("Operasyon:")
print("1: Topla")
print("2: Çıkar")
print("3: Çarp")
print("4: Böl")

secenek = input("Operasyon Seciniz?")

sayi1=int(input("Birinci Sayınızı girin: "))
sayi2=int(input("İkinci Sayınızı girin: "))

if (secenek == '1'):
    
    print=("Sonuç : " + str(topla(sayi1,sayi2))) 
    
elif (secenek=="2"):
    print=("Sonuç : "  ,cikar(sayi1,sayi2))
    
elif (secenek=="3"):
    print=("Sonuç : "  ,carp(sayi1,sayi2)) 
    
elif (secenek=="4"):
    print=("Sonuç : "  ,bol(sayi1,sayi2))     
    
else:
    print("Hatalı veya yanlış bir işlem yaptınız.Uygulamadan çıkılıyor...")
