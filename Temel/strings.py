# -*- coding: utf-8 -*-

mesaj="Merhaba Dünya!"
##replace upper and lower
yeniMesaj= mesaj[0:7]
yeniMesaj2=mesaj[-1:]
print(yeniMesaj)
print(yeniMesaj2)
print(mesaj.lower())
mesaj=mesaj.replace("ü","u")
#message replace
print(mesaj)
print(mesaj.replace("a","e"))

#split ve strip
bilgi ="Engin;Demiroğ;33;Ankara ".strip()

bilgi=bilgi.split(";")
print("Adı = " + bilgi[0])

#input
ad=input("Adınız ?")
sayi1=input("Sayi 1 = ?")
sayi2=input("Sayi 2 = ?")
print(int(sayi1) + int(sayi2))



