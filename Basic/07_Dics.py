#Estructuras clave:valor 
my_dict = {}
my_other_dict = dict ()
print(type(my_dict)) 

my_dict = {"Nombre":"Franco", "Apellido": "Rizzi", "Edad":27, 1: "Boka"}
print(my_dict)
my_other_dict = {
    "Nombre":"Franco",
      "Apellido": "Rizzi", 
      "Edad":27,
    "Club": {"Boka", "Estudiantes", "Scaloneta"}
    }
print (my_other_dict)
print (len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])
print (my_other_dict["Club"])

my_dict["Apellido"] = "Zingaretti"
print((my_dict["Apellido"]))

my_dict ["Pais"] =  "Italia"
print (my_dict)

del my_dict ["Pais"]
print(my_dict)

print ("Rizzi"in my_dict)
print ( "Apellido" in my_dict) 

print (my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print (my_other_dict.fromkeys(("Nombre",1)))


my_list =  ["Nombre", 1, "Pais"]


my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict,("Franco", "Rizzi"))
print (my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print (set(my_new_dict))