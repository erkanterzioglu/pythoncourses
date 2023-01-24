sayi1=int(input("1.sayinizi girin"))
sayi2=int(input("2.sayinizi girin"))
sayi3=int(input("3.sayinizi girin"))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk=sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk=sayi2
else:
    enBuyuk=sayi3
    
print("En Büyük " + str(enBuyuk))