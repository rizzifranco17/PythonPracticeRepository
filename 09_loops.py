#WHile
my_condition = 0 

while my_condition <10:
    print(my_condition)
    my_condition += 2 
if my_condition == 10:
    print ("My condition es igual a 10")
else:
    print("My condition es mayor o igual a 10")
print ("next")

while my_condition < 20:
    my_condition+=1
    if my_condition == 15:
        print ("STOP")
        break

    print (my_condition)
print ("The end")

#For 
my_list = [35,24,62,52,30,17]

for element in my_list:
    print(element)

my_tuple = (27,1.77, "Franco", "Rizz", "Tano")
for element in my_tuple:
    print (element)
my_set = {"Franco", "Rizz",35}
for element in my_set:
    print (element)
my_dict = {"Nombre":"Franco", "Apellido":"Rizzi", "Edad": 27}
for element in my_dict:
    print (element)
    if element == "Edad":
        break
    print ("Execution")
else:
    print ("The End")