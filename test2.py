# # 1задание 
class KgToPounds:
    def __init__(self,kg):
        self.__kg=kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Киллограммы задаются только числами") 

    def get_kg(self):
        return self.__kg

    def property(self):
        kg=property(get_kg, set_kg )

kg=KgToPounds(12)



# # 2 задание
class Math:
    def __init__(self, a, b):
        self.a=a
        self.b= b
    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b

mat=Math(12,2)
print(mat.__sub__())

# 3 задание

class Soda:
    def __init__(self, dobavka):
        self.dobavka = dobavka

    def show_my_drink(self):
        if self.dobavka == self.dobavka:
            print(f"Газировка и {self.dobavka}")
        else:
            print(f"Обычная газировка")

sod=Soda("лимон")
print(sod.show_my_drink())
         
# 4 задание  
class Name:  
    def __init__(self, age = 0):  
         self._age = age   
    def get_age(self):  
        return self._age  
     
    def set_age(self, a):  
        self._age = a  
   
John = Name()  
   
John.set_age(19)     
print(John.get_age())    
print(John._age)

# 5 задание
class Auto:
    def ride(self):
        print("Riding on a ground")
       

class Boat:
    def swim(self):
        print("Sailing in the ocean")

class Amphibian(Auto, Boat):
    pass
 
a = Amphibian()
a.ride()
a.swim()        