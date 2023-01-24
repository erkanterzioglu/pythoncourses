class  Matematik:
    
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        
        print("Çalıştı")
        
    def topla(self):
        return self.sayi1+self.sayi2 
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1*self.sayi2
    
    def bol(self):
        return self.sayi1/self.sayi2
    
math=Matematik(2,18)
print("Toplam: ",math.topla())

#%% Poperty

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName=firstName 
        self.lastName=lastName
        self.age=age
        
        
person1= Person("Erkan","Terzi",22)
print(person1.firstName,person1.lastName,person1.age)



class Worker(Person):
    def __init__(self,salary):
        self.salary=salary
        
class Customer(Person):
    def __init__(self,creditCardNumber)
        self.creditCardNumber=creditCardNumber
        
        
ahmet=Worker()
mehmet=Customer()



        
        
        