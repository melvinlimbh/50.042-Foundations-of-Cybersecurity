# 50.042 FCS Lab 6 template
# Year 2021

import random
def square_multiply(a,x,n):
    """
    y = 1

    n_b is the number of bits in x
    for( i = n_b-1 downto 0 )

    # square
    y = y^2 mod n
    # multiply only if the bit of x at i is 1
    if (x_i == 1) y = a*y mod n
  
    return y

    i.e 
    LOOP for bits in x:
    y = y**2 mod n
    if bits in x == 1, multiply 
    """
    y = 1
    bits_of_x = bin(x)[2:]

    for bit in bits_of_x:
        y = pow(y,2) % n
        if bit == "1": 
            y = (a*y) % n
        else: continue

    return y

def miller_rabin(n, a):
    """
    probabilistic test to determine if a number is likely to be prime

    n = integer to check, a = number of rounds

    Input: odd integer n>=3
    1. find odd u such that n-1 = 2^k * u 
    2. Choose a random int, where 1<x<n-1
    3. b = x^u mod n
    4. if b==1 or b== n-1 return probable prime
    5. repeat k-1 times
    6.     b = b^u mod n
    7.     if b=n-1 return probably prime
    8.     if b=1 return not prime
    9. return not prime

    reference: https://justcryptography.com/miller-rabin-test/
    """
    if n == 2: return True
    elif n%2 == 0 : return False

    u, k, b = n-1, 0, 0
    while (u%2 == 0):
        u //= 2
        k += 1

    for i in range(a):
        x = random.randint(2,n-2)
        b = pow(x,u,n)

        if b == 1 or b == n-1: 
            continue

        for j in range(k):
            b = pow(b,2,n)
            if b == n-1: break

        else: 
            return False

    return True

def gen_prime_nbits(n,output = 0):
    
    is_prime = miller_rabin(output,2)

    if is_prime: 
        #print(output.bit_length())
        return output

    else:
        output = random.getrandbits(n)
        return gen_prime_nbits(n,output)

if __name__=="__main__":
    print('Is 561 a prime?')
    print(miller_rabin(561,2))
    print('Is 27 a prime?')
    print(miller_rabin(27,2))
    print('Is 61 a prime?')
    print(miller_rabin(61,2))

    print('Random number (100 bits):')
    print(gen_prime_nbits(100))
    print('Random number (80 bits):')
    print(gen_prime_nbits(80))