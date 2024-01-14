number_one = 5
number_two = "1"
#number_two = 4
try: 
    print(number_one +number_two)
    print("Execution succes")
except: 
    print(" Error, check inputs")
else: #opcional
    print ("Excecution continue")
finally: #opcional
    print ("Execution complete")
# Exceptios for type
try: 
    print(number_one +number_two)
    print("Execution succes")
except ValueError: 
    print(" ValueError, check inputs")
except TypeError: 
    print(" TypeError, check inputs")
#Capture of error
try: 
    print(number_one +number_two)
    print("Execution succes")
except ValueError: 
    print(" ValueError, check inputs")
except Exception as error: 
    print(error)