import re 

def check_password_strenght (password):
    if len(password) < 9:
        return "Weak: Password must be at least 7 characters long."
    
    if not re.search(r'[A-Z]', password):
        return "Weak:Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return "Weak:Password must contain at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
     return "Weak:Password must contain at least one special character."
    
    if not re.search(r'[0-9]', password):
        return "Weak: Password must contain at least one digit."
    
    return "Strong Password!"

password = input ("Enter a password to check its strength:")
print (check_password_strenght(password))

    
