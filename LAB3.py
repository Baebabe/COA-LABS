#Multipluication of two 4 bit binary numbers

def xor(a, b):
    return (a and not b) or (not a and b)

def half_adder(a, b):
    s = int(xor(a, b))
    c = int(a and b)
    return s, c

def full_adder(a, b, ci):
    s1, c1 = half_adder(a, b)
    s, c2 = half_adder(s1, ci)
    co = int(c1 or c2)
    return s, co

def eightbitadder(i1, i2):
    S = [0] * 8
    carry = 0
    for i in range(7, -1, -1):
        S[i], carry = full_adder(i1[i], i2[i], carry)
    return S

def multiplier(i1, i2):
    P = [0] * 8 
    for x in range(4):
        if i2[3 - x] == 1:
            shifted_M = ([0] * x) + i1 + ([0] * (4 - x))
            shifted_M = shifted_M[:8] 
            P = eightbitadder(P, shifted_M)
    return P

i1 = [1, 1, 0, 1] 
i2 = [1, 0, 1, 0]  
product = multiplier(i1, i2)
print("Product:", product) 
