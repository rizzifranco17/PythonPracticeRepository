import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(hash_to_crack, wordlist):
    with open(wordlist, 'r')as file:
        for word in file:
            word = word.strip()
            if hash_password(word) == hash_to_crack: 
                return f"Password found : {word}" 
    return "Password not found"

hash_to_crack = input ("Enter the SHA-256 hash to crack: ")
wordlist_path = input ("Enter the path to your wordlist file: ")
print (brute_force(hash_to_crack, wordlist_path))
