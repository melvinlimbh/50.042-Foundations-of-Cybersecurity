from Crypto.PublicKey import RSA

def square_multiply(a,x,n):
    y = 1
    for i in bin(x)[2:]:
        y = (y*y)%n

        if (i == '1'):
            y = (y*a) % n

    return y
# public key

def encrypt(x,e,n):
    return square_multiply(x,e,n)

def decrypt(x,d,n):
    return square_multiply(x,d,n)


# public key
key1 = open('mykey.pem.pub','r').read()
rsakey_pub = RSA.importKey(key1)
print("public key")
print(f"rsakey.n : ,{rsakey_pub.n}")
print(f"rsakey.e : {rsakey_pub.e}")

# private key
key2 = open('mykey.pem.priv','r').read()
rsakey_priv = RSA.importKey(key2)
print("private key")
print(f"rsakey.n : {rsakey_priv.n}")
print(f"rsakey.d : {rsakey_priv.d}")

print ("-------------------------------------Part II-----------------------------------")
print("encrypting:  100")
y = encrypt(100, rsakey_pub.e, rsakey_pub.n)
y_s = encrypt(2, rsakey_pub.e, rsakey_pub.n)
m = y * y_s

m_decrypted = decrypt(m, rsakey_priv.d, rsakey_priv.n)
print(f"result:\n{y}\n")
print(f"modified to:\n{m}\n")
print(f"decrypted:  {m_decrypted}")