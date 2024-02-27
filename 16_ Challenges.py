'''Write a program thtat shows in the console
*Numbers from 1 to 100 (both included with a line jump
beetween each print)
* multiple of 3 change for : fizz
*multiple of 5 chanche for buzz
* multiple of 3 and 5 change it for fizzbuzz'''

def fizzbuzz():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print ("fizzibuz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print ("buzz")    
        else:
            print (i)

fizzbuzz()


