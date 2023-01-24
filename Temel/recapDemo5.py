# -*- coding: utf-8 -*-

import sys

liste=['erkan',0,3,"6"]

for x in liste:
    try:
        print("Sayı"+ str(x) )
        sonuc=1/int(x)
        print("Sonuç: "+ str(sonuc))
    except ValueError:
        print(str(x)+"için  değer hatası ")
    except ZeroDivisionError :
        print(str(x) +" için payda Sıfır olamaz!")
    finally:
        print("İşlem tamamlandı")