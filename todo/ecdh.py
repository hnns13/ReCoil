# ECDH key will replace static key of crpyto.py
# crpytography program is being restructured to use ECDH for key exchange 

def multiply_point(P, k, p, a): #double-and-add
    result = (0, 0)
    while k > 0:
        if (k & 1) == 1: # Fall: Das niedrigstwertige Binärbit von k ist 1 → addiere P
            result = add_points(result, P, p, a) # Verdoppele P für das nächste Bit von k
        P = add_points(P, P, p, a) # Verdopple P für das nächste Bit von k
        k >>= 1 # Rechtsverschiebung von k um 1 Bit (entspricht Division durch 2)
    return result

def add_points(P1, P2, p, a):

    if P1 == (0, 0):
        return P2 
    if P2 == (0, 0):
        return P1 
    r1, s1 = P1 
    r2, s2 = P2 
    if P1 == P2:
        m = ((3 * r1 * r1)+ a)* modinv(2 * s1, p) % p # Steigung bei Verdopplung des Punktes (2*P) 
    else:
        m = (s2 - s1) * modinv(r2 - r1, p) % p # Steigung bei Addition zweier Punkte (P + Q) 
    r3 = (m * m - r1 - r2) % p 
    s3 = (m * (r1 - r3) - s1) % p 
    return (r3, s3)

def erw_euklid(a, b):
    if a == 0: 
        return b, 0, 1 
    g, x1, y1 = erw_euklid(b % a, a)
    x = y1 - (b // a) * x1 
    y = x1 
    return g, x, y # Rückgabe des GGT und der Koeffizienten. Für den rekursiven Aufruf braucht es diese Rückgabe.

def modinv(a, p): 
    a = a % p
    g, x, y = erw_euklid(a, p)
    return x % p 

if __name__ == "__main__":

    a= 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc # Basisparameter seckp256k1
    G = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5) # Basisparameter seckp256k1
    p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff # Basisparameter seckp256k1

    exit