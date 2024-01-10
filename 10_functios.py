
def my_function ():
    print("Esto es una funcion")

my_function()


def sum_two_values (first_value, second_value):
    print (first_value * second_value)

sum_two_values(4,2)
sum_two_values (4, 3)

def sum_two_values_with_return (first_value,second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return (10,5)
print (my_result )

def print_name(name,lastname):
    print (f"{name} {lastname}")
print_name ("Franco", "Rizzi")

def print_name_with_default (name, lastname, alias="sin alias"):
    print (f"{name} {lastname} {alias}")
print_name_with_default ("Franco", "Rizzi")

def print_texts(*texts): # * means its dinamic and we can put infinit
    for text in texts:
        print (text.upper())
print_texts ("hola","Tano", "Skeree")

