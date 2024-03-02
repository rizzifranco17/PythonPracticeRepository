
sum_two_values = lambda first_value, second_value:  first_value + second_value

print  (sum_two_values(11,4))


multiple_values = lambda first_value, second_value: first_value * second_value - 3
print (multiple_values (3,3)) 

def sum_three_values(value): 
    return lambda first_value, second_value: first_value + second_value + value

print (sum_three_values (5)(2,4))
