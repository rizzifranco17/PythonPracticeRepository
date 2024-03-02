'''Escribe un programa que se encargue de comprobar si un numero
es o no primo. 
Hecho estom impre los numeros primos entre 1 y 100'''



def is_prime():
    for number in range (1,100):

 
        if number >= 2:
         
            is_divisible = False 
            for index in range (2,number):

             if number % index == 0:
                 is_divisible =  True
                 break   
            if not is_divisible:
                 print (number)   
    

is_prime()