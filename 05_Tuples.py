my_tuple = tuple ()
my_other_tuple = ()

my_tuple = (27, 1.80, "Franco", "Rizzi")

my_other_tuple = (27,25,23,29,31,33)
print (my_tuple)
print (type(my_tuple))
print(my_tuple[1])
print (my_tuple[-2])

print(my_tuple.count(27))
print(my_tuple.index("Franco"))

#my_tuple [1] = 1.80 
'''Con las tuplas los valores son fijos no se pueden cambiar. 
Esa es la diferencia con las listas'''

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[1:7])

my_tuple = list (my_tuple)
my_tuple[3] = "Tano"
my_tuple.insert(3, "apodo")
my_tuple = tuple(my_tuple)
print (tuple(my_tuple))

