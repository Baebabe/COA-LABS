#SUBTRACTION OF TWO UNSIGNED INTEGER BINARY NUMBER

def halfadder(a, b):
    sum = int((not a and b) or (a and not b))
    carry = int(a and b)
    return sum, carry

def fulladder(a, b, c):
    sum1, carry1 = halfadder(a, b)
    sum2, carry2 = halfadder(sum1, c)
    carry = int(carry1 or carry2)
    return sum2, carry

def _2scomp(num):
    n1 = [not bit for bit in num]
    n2 = [0, 0, 0, 1]
    s, _ = fourbitadder(n1, n2)
    return s

def fourbitadder(num1, num2):
    s = [0, 0, 0, 0]
    c = 0
    for i in range(3, -1, -1):
        s[i], c = fulladder(num1[i], num2[i], c)
    return s, c

num1 = [1, 0, 0, 0]
num2 = [1, 0, 0, 0]
num3 = _2scomp(num2)
sum, _ = fourbitadder(num1, num3)
print(sum)
