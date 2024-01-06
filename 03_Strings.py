#Strings 
my_string = "Mi string"
my_other_string = "Mi otro string"
print(len(my_string))
print(len(my_string + my_other_string))

my_new_string = "Este es un string\ny esto se escribe abajo" #con \n puedo hacer que se escriba abajo
print(my_new_string)


my_tab_string = "\tEste es un string y esto se escribe abajo" #con \t puedo hacer una sangria 
print(my_tab_string)

name, lastname, libertadores= "Boka", "Jrs", 6

print ("Mi club es {} {} y tengo {} libertadores".format(name,lastname,libertadores))
print ("Mi club es %s %s y tengo %d libertadores" %(name,lastname,libertadores))

#Desempaquetado de carcteres
Lenguaje = "pyhton"
a,b,c,d,e,f = Lenguaje
print (a)
print (e)

#Corte de palabras
language_slice = Lenguaje [0:4]
print(language_slice)
language_slice = Lenguaje [0:]
print(language_slice)
language_slice = Lenguaje [-4] #Con el signo negativo arranca del final 
print(language_slice)

reversed_lenguage = Lenguaje [::-2]
print (reversed_lenguage)

#Funciones
print (Lenguaje.capitalize())
print (Lenguaje.upper())
print (Lenguaje.count("t"))
print (Lenguaje.isnumeric())
print ("3".isnumeric()) 
print (Lenguaje.lower())
print (Lenguaje.upper().isupper())