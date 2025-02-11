def caesar_cipher (text,shift):
    encrypted_text = ""
    for char in text: 
        if char.isalpha():
            shift_base = ord ('A')if char.isupper() else ord ('a')
            encrypted_text += chr((ord(char)-shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

text = input ("Enter the text to encrypt: ")
shift = int (input("Enter the shift value:"))
print ("Encrypted text:", caesar_cipher(text,shift))