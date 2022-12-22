# 50.042 FCS Lab 6 template
# Year 2021

from math import ceil,sqrt
import primes

def baby_step(alpha, beta, p, fname):
    """
    Calculate m = ceiling(sqrt(|p-1|))
    Baby-step phase: Compute and store into a file the values of 
    pow(alpha,xb)*β where 0 ≤ xb < m
    """
    m = ceil(sqrt(p-1))
    with open(fname, mode = "w") as f:
        for xb in range(m):
            f.write(str(((alpha**xb)*beta)%p) + "\n")

def giant_step(alpha, p, fname):
    """
    Calculate m = ceiling(sqrt(|p-1|))
    Giant-step phase: Compute and store into a file the values of 
    pow(alpha,mx*xg), where 0 ≤ xg < m
    """
    m = ceil(sqrt(p-1))
    with open(fname, mode = "w") as f2:
        for xg in range(m):
            f2.write(str(primes.square_multiply(alpha,m*xg,p)) + "\n")

def baby_giant(alpha, beta, p):
    """
    call baby_step and giant_step
    Check the outputs and see if there is a match, calculate x = xgm - xb
    xb and xg are index values
    """
    m = ceil(sqrt(p-1))
    baby_step(alpha, beta, p, "baby_step.txt")
    giant_step(alpha, p, "giant_step.txt")

    with open("baby_step.txt",mode="r") as f1:
       baby_ls = [line.rstrip("\n") for line in f1.readlines()]

    with open("giant_step.txt",mode="r") as f2:
        giant_ls = [line.rstrip("\n") for line in f2.readlines()]

    match = list(set(baby_ls).intersection(set(giant_ls)))
    print(match)

    if len(match) > 0:
        xb = baby_ls.index(match[0])
        xg = giant_ls.index(match[0])

    return xg*m - xb

if __name__ == "__main__":
    """
    test 1
    My private key is:  264
    Test other private key is:  7265
    """
    p = 17851
    alpha = 17511
    A = 2945
    B = 11844
    sharedkey = 1671
    a = baby_giant(alpha, A, p)
    b = baby_giant(alpha, B, p)
    guesskey1 = primes.square_multiply(A, b, p)
    guesskey2 = primes.square_multiply(B, a, p)
    print("Guess key 1:", guesskey1)
    print("Guess key 2:", guesskey2)
    print("Actual shared key :", sharedkey)
