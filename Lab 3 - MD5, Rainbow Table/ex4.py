import random
import time
import string
import hashlib

def hash(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()

def attack(criteria, hashed_text):
    for char1 in criteria:
        for char2 in criteria:
            for char3 in criteria:
                for char4 in criteria:
                    for char5 in criteria:
                        plaintext = char1 + char2 + char3 + char4 + char5

                        hash_attack = hash(plaintext)

                        if hash_attack in hashed_text:
                            hashed_text.remove(hash_attack)

                        if len(hashed_text) == 0:
                            return 0
    return 0
    
if __name__ == "__main__":

    with open(r"C:\Users/user/Downloads\Lab\lab3\ex2_hash.txt", "r", encoding="utf-8", newline="\n") as f:
        
        salt = random.choice(string.ascii_lowercase)
        new_plaintext = set([(line.strip() + salt) for line in f])
    
        with open(r"C:\Users/user/Downloads\Lab\lab3\salted6.txt", "w", encoding = "utf-8", newline = "\n") as f2:
            with open(r"C:\Users/user/Downloads\Lab\lab3\plain6.txt", "w", encoding = "utf-8", newline = "\n") as f3:
                for item in new_plaintext:
                    rehash = hash(item)
                    f2.write(rehash + " || salt: " + salt + "\n")
                    f3.write(item + "\n")