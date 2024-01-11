class Person :
    pass

class MyPerson: 
    def __init__(self, name,lastname):
        self.name = name
        self. lastname = lastname

my_person = MyPerson("Franco", "Rizzi")
print (f"{my_person.name}, {my_person.lastname}")
print(my_person.lastname)


class MyPerson2:
    def __init__(self):
        self.name = "Malena"
        self.lastname = "Espinosa"
my_person2= MyPerson2()
print (f"{my_person2.name}{my_person2.lastname}")

class MyPerson3:
    def __init__(self, name, lastname, alias = "sin alias") :
        self.full_name = f"{name} {lastname} ({alias })"
    def walk (self):
        print(f"{self.full_name} Esta caminando")
my_person3 = MyPerson3 ("Franco", "Zingaretti", "Tano")  

print (my_person3.full_name)    

my_person3.walk ()
my_person3.full_name = "Malena Espinosa"
print (my_person3.full_name)