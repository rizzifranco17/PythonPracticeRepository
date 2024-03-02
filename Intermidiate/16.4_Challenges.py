'''Crea un programa que invierta l orden de una cadena de texto 
sin usar funciones propias del lenguaje que lo hagan de froma automatica
Si le pasamos "Hola mundo" devolveria "odnum aloH"'''


def reverse (text):
    text_len = len (text) - 1
    reversed_text = ""
    for index in range (0, len(text)):
        reversed_text += text [text_len - index]
    return reversed_text
    
    


print (reverse("Hola mundo"))