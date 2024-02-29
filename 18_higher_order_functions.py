

from functools import reduce


def sum_one (value):
    return value + 1

def sum_five (value):
    return value + 5

def sum_two_values_and_one (first_value, second_value,f_sum):
    return f_sum (first_value + second_value)

print (sum_two_values_and_one(3,2,sum_one))
print (sum_two_values_and_one(3,2,sum_five))

# Closures # 

def sum_ten (original_value): 
    def add (value):
        return value + 10 + original_value
    return add
 #Function returnig function 
add_closure = sum_ten (10)
print (add_closure(15))

# Build-in Higher Order Functions 

number = [2,5,10,21,3,45]

# Map

def multuply_by_two (number):
    return number * 2


#print(list( map (multuply_by_two,number)))

print(list( map (lambda number :number *2,number)))
# I can use a lambda a get the same result without defining another function 
#Filter 
def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False
print(list (filter (filter_greater_that_ten, number)))
print(list (filter (lambda number: number >10, number)))

#Reduce

[2,5,10,21,3,45]

def sum_two_values (first_Value, second_value):
    print (first_Value)
    print (second_value)
    return first_Value + second_value

print(reduce (sum_two_values,number))
