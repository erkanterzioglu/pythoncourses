sayi=int(input("Sayı giriniz: "))

for x in range(2,sayi):
    asalMi="evet"
    if (sayi %x ) ==0:
        print("Bu sayı asal değildir")
        break
    elif(asalMi == "evet"):
        print("Bu sayı asaldır")
        break
    
    

