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
                            print (hash_attack,'=',plaintext)
                            hashed_text.remove(hash_attack)

                        if len(hashed_text) == 0:
                            return 0
    return 0
    
if __name__ == "__main__":

    with open(r"C:\Users/user/Downloads\Lab\lab3\hash5.txt", "r", encoding="utf-8", newline="\n") as f:
        hashed_text = set([line.strip() for line in f])
        
    start_time = time.perf_counter()
    criteria = string.ascii_lowercase + string.digits
    attack(criteria, hashed_text)
    end_time = time.perf_counter()
    print('Time taken: {}'.format(end_time-start_time))