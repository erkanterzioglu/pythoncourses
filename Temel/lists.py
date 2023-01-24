ogrenci1="Engin"
ogrenci2="Derin"
ogrenci3="Salih"

print(ogrenci1)
print(ogrenci2)
print(ogrenci3)

ogrenciler= ["Engin","Derin","Salih"]
#ogrenci ekleme komutu
print(ogrenciler[1])
ogrenciler.append("Ahmet")
print(ogrenciler[3])
#remove komutu
ogrenciler.remove("Salih")


print(ogrenciler)

#List constructor
sehirler =list(("Ankara","İstanbul"))
print(sehirler)

#diğer fonksiyonlar
# print(sehirler.clear())

print("Ankara sayısı= " + str(sehirler.count("Ankara")))
print("Ankara indexi= " + str(sehirler.index("Ankara")))
sehirler.pop(1)
sehirler.insert(0,"İstanbul")
sehirler.reverse()
print(sehirler)
sehirler2=sehirler
sehirler2[0]="İzmir"
print(sehirler)
sehirler3=sehirler.copy()
print(sehirler3)
sehirler.extend(sehirler3)
print(sehirler)
sehirler.sort()
sehirler.reverse()
print(sehirler)
