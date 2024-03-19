
my_string_variable = "My string variable"
print (my_string_variable)
print (type(my_string_variable))

my_string_variable = 7 
print(my_string_variable)
print (type(my_string_variable))

my_other_variable : str = 8
my_other_variable
print (my_other_variable)
print (type(my_other_variable))
my_other_variable = 5 
print (my_other_variable)
print (type(my_other_variable))


def get_full_name (first_name : str , last_name : str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name
print (get_full_name("franco", "rizzi"))
