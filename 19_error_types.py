

#SyntaxError

#print "Hello World"
print("Hello World")

#NameError
name = "LeoMessi" #Uncoment for error
print(name)

#IndexError

my_list = ["Python","Go","Swift","Java"]
print(my_list[-2])
print(my_list[1])
#print(my_list[4]) IndexError since this number is out of range

#ModuleNotFoundError

# import maths 
import math

#AttributeError

#print (math.PI)
print (math.pi)

#KeyError
my_dict = {"Nombre" : "Franco", "Surname": "Rizzi", "Languaje": "Python"}
print (my_dict["Nombre"])
#print(my_dict["Surnam"])

#TypeError
#print (my_list["Nombre"])  List take integers not str

#importError
#from math import PI
from math import pi
print(pi)

#ValueError
my_int = int ("10")
#my_int = int ("10 años")
print(type(my_int))

#ZeroDivisionError
print(4/2)
#print(4/0)