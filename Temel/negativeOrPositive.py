# -*- coding: utf-8 -*-

sayi=int(input("Herhangi bir sayı girin"))

print(sayi)

if (sayi<0):
    print("Girdiğiniz sayı<"+str(sayi)+"> negatiftir.")
elif(sayi>0):
    print("Girdiğiniz sayi<" + str(sayi)+"> pozitifitir.")
else:
    print("Girdiğiniz sayı sıfırdır.")    