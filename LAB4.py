#Retstoring division

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
    carry = 0
    S = [0] * max_len
    for i in range(max_len - 1, -1, -1):
        S[i], carry = fulladder(A[i], B[i], carry)
    return S

def restoring_division(Q, M):
    n = len(Q)
    A = [0] * n
    Minus_M = twos_complement(M)
    for _ in range(n):
        A = shift_left(A)
        A[-1] = Q[0]
        Q = shift_left(Q)
        A = binary_addition(A, Minus_M)
        if A[0] == 1:
            A = binary_addition(A, M)
            Q[-1] = 0
        else:
            Q[-1] = 1
    return Q, A

def take_input():
    num1 = input("Enter dividend in binary number: ")
    num2 = input("Enter divisor in binary number: ")
    A = [int(x) for x in num1]
    B = [int(x) for x in num2]
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    return A, B

dividend, divisor = take_input()
quotient, remainder = restoring_division(dividend, divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)
