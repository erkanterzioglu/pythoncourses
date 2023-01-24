# -*- coding: utf-8 -*-

sehir="Ankara"

print(sehir.upper())
print(sehir.endswith("e"))


def selamVer(x="Ziyaretçi"):
    print("Merhaba "+x )
    
selamVer("Erkan")
selamVer()


#%%
def dikUcgenHesapla(a=(int(input("Kenar1 girin"))), b=(int(input("Kenar2girin")))):
    return a*b/2

print(dikUcgenHesapla())

#%%

