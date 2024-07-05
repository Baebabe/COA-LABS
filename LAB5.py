#Non Restoring Division

def halfadder(a, b):
    sum = int((not a and b) or (a and not b))
    carry = int(a and b)
    return sum, carry

def fulladder(a, b, c):
    sum1, carry1 = halfadder(a, b)
    sum2, carry2 = halfadder(sum1, c)
    carry = int(carry1 or carry2)
    return sum2, carry

def shift_left(A):
    return A[1:] + [0]

def twos_complement(A):
    A = [not(bit) for bit in A]
    A = binary_addition(A, [0] * (len(A) - 1) + [1])
    return A

def binary_addition(A, B):
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    Cin = 0
    S = []
    for i in range(max_len-1, -1, -1):
        sum, Cin = fulladder(A[i], B[i], Cin)
        S.insert(0, sum)
    return S

def non_restoring_division(Q,M):
    A=[0]*len(Q)
    next="sub"
    Minus_M=twos_complement(M)
    for i in range(len(Q)):
        A=shift_left(A)
        A[-1]=Q[0]
        Q=shift_left(Q)
        if next=="sub":
            A=binary_addition(A,Minus_M)
        else:
            A=binary_addition(A,M)
        if A[0]==1:
            next="add"
            Q[-1]=0
        else:
            next="sub"
            Q[-1]=1

        if i==len(Q)-1:
            if(next=="add"):
                A=binary_addition(A,M)
    
    return Q,A


def take_input():
    num1 = input("Enter dividend in binary number: ")
    num2 = input("Enter divisor in binary number: ")
    A = [int(x) for x in num1]
    B = [int(x) for x in num2]
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    return A, B

dividend,divisor=take_input()
print(dividend,divisor)
quotient,remainder=non_restoring_division(dividend,divisor)
print(quotient,remainder)
