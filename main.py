class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age

studenti1 = Student("Dior", 15)

print("Name:",studenti1.get_name())
studenti1.set_name("Dion")
print("Emri i vertet eshte:",studenti1.get_name())

print("Age:",studenti1.get_age())
studenti1.set_name("Dion")
print("Mosha e vertet eshte:",studenti1.get_age())