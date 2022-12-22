# 50.042 FCS Lab 6 template
# Year 2021

import primes
import random

def dhke_setup(nb):
    """
    nb = number of bits
    generate a large prime p
    generate an integer alpha ∈ {2, 3, . . . , p-2}
    return the values of p and alpha
    """
    p = primes.gen_prime_nbits(nb)
    alpha = random.randint(2,p-2)

    return p,alpha

def gen_priv_key(p):
    """
   Choose a random private key: a ∈ 2, ... , p-2
    """
    return random.randint(2,p-2)

def get_pub_key(alpha, a, p):
    """
    Compute the first public key: A  ≡ (a**alpha) mod p
    """
    return pow(a,alpha,p)

def get_shared_key(keypub, keypriv, p):
    """
    compute the shared keys: kAB ≡ Ba mod p
    """
    return ((keypriv*keypub) % p)


if __name__ == "__main__":
    p, alpha = dhke_setup(80)
    print("Generate P and alpha:")
    print("P:", p)
    print("alpha:", alpha)
    print()
    a = gen_priv_key(p)
    b = gen_priv_key(p)
    print("My private key is: ", a)
    print("Test other private key is: ", b)
    print()
    A = get_pub_key(alpha, a, p)
    B = get_pub_key(alpha, b, p)
    print("My public key is: ", A)
    print("Test other public key is: ", B)
    print()
    
    sharedKeyA = get_shared_key(B, a, p)
    sharedKeyB = get_shared_key(A, b, p)
    print("My shared key is: ", sharedKeyA)
    print("Test other shared key is: ", sharedKeyB)
    print("Length of key is %d bits." % sharedKeyA.bit_length())
