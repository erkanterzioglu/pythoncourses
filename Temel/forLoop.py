# -*- coding: utf-8 -*-

sehirler =["Ankara","İstanbul","İzmir"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])


#%%
for sehir in sehirler:
    if (sehir == "İstanbul"):
        print(sehir +" "+ "için kod = " + sehir[0:3])
        print("**********")
    
#%%
for x in range(1,101,2):
    print(x)