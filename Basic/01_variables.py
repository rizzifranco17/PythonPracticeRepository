my_string_variable = "Bokaaa"
my_int_variable = 7
print (my_int_variable)
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False 
#Concatenacion de impresion de variables
print (my_string_variable,my_int_to_str_variable,my_bool_variable)
#Funciones del sistema len 
print (len(my_string_variable))
print("Este es el valor de:", my_bool_variable) 

#Variables de una sola linea 
name, lastname, apodo, edad = "Franco", "Rizzi", "Tano", 27
print("Mellamo:",name,lastname,edad,"Mi apodo es:", apodo)

#Inputs
name = input ('Cuales es tu nombre?')
edad = input ('Cuantos años tienes?')

print(name)
print (edad)

address: str = "Mi dirección"
address = 32
print (type(address))