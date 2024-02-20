
my_list = list()
my_other_list = []

print (len(my_list))
print (len(my_other_list))

my_list = [23,45,20,33, 19,23]

print(my_list)
print (len(my_list))

my_other_list = [27,1.82, 'franco', 'Rizzi']
print (type(my_other_list))

print(my_other_list[0])
print(my_other_list[-3])
print(my_other_list.count('Rizzi'))
print (my_list.count(23)) #Count es para contar elementos en la propia lista 

age, height, name, lastname = my_other_list
print (name)

print(my_list + my_other_list)

my_other_list.append("Boka")
print (my_other_list)

my_other_list.insert(2, "Córdoba")
print (my_other_list)
my_other_list [2] = "Rio Cuarto"
print(my_other_list)
my_other_list.remove ("Rio Cuarto")
print(my_other_list)
my_other_list.pop()
print(my_other_list.pop(0)) #forma de eliminar elemento en un lugar especifico 
print (my_other_list)

del my_other_list [0] #Elimina elementos de la lista por ubicacion
print (my_other_list)

my_new_list = my_other_list.copy ()
my_other_list.clear()
print (my_other_list)
print(my_new_list)
my_new_list.reverse ()
print(my_new_list.reverse()) 

my_new_list.sort ()
print(my_new_list)
my_list.sort ()
print(my_list)




my_list = "Hello Python"
print(type (my_list)) #Demostracion de lenguaje dinamico
