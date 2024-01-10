#No es una estructura ordenada
my_set = set()
my_new_set = {}

my_new_set = {"Franco","Rizzi", 27}
print(type(my_new_set))

print(len(my_new_set))
my_new_set.add ("Tano")
print(my_new_set)
my_new_set.add ("Tano") #Set no admite repeticiones 
print(my_new_set)
my_new_set.remove (27)
print (my_new_set)
print (27 in my_new_set)
print("Franco"in my_new_set)
del my_new_set

my_set = {"Boca", "Estudiantes", 7}
print (my_set)
my_list = list (my_set)
print(my_list)
print (my_list[2])

my_other_set = {"Español", "Ingles", "Italiano"}
my_new_set = my_set.union (my_other_set)
print(my_new_set.union({"Cordobes"}))

print (my_new_set.difference(my_other_set))