
my_original_list = [0,1,2,3,4,5,6,7]

my_list = [i for i in range(7)]
print(my_list)

my_range = range (7)
print (list(my_range))


def sum_five (number):
    return number + 5

my_list = [sum_five (i)for i in range(8)] #You can do other operations ( +,-,/,*)
print(my_list) 

