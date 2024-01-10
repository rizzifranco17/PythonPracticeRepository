auth = False
Username = input ("Insert your username")
Password = input ("Insert your Password")

print (Username + " " + Password)

if Username == "FrancoRizzi" and Password == "12345":
 auth =True
else:
    print ("Usuario y/o contraseña no valido. 2 Intentos restants")
    print ("Insert your username")
    Username = input ()
    print ("Insert your password")
    Password = input ()

if Username == "FrancoRizzi" and Password == "12345":
    print ("Bienvenido al sistema")
else:
    print ("Usuario y/o contraseña no valido. 1 Intentos restants")
    print ("Insert your username")
    Username = input()
    print ("Insert your passsword")
    Password = input ()
    if Username == "FrancoRizzi" and Password == "12345":
        print ("Welcome to the sistem")
    else:
        print ("You have been blocked")

if auth :
        print ("Bienvenido al sistema")
balance = 2000
print ("What do you wanna do ? ")
print("1. Deposit")
print("2.WithDraw")
print("3.View")
print("4.Transfer")
print ("5.Exit")
option = input ()
if option == "1":
    print ("cuanto quiere depositar")
    deposit = int(input())
    balance += deposit
    print (f"Your balance is {balance}")
elif option == "2":
        print ("How much do you want to withdraw?")
        withdraw = int(input())
        balance -= withdraw
        print (f"Your balance is {balance}")
elif option == "3":
     print (f"Your balance is {balance}")
elif option == "4":
     print ("How much you wanna transfer?")
     transfer = int(input())
     balance -= transfer 
     print (f"Your balance is {balance}")
elif option == "5":
     print ("Nos vimo")
print ("Thanks four using this service")

