# Booth's Algorithm

def halfadder(a, b):
    sum = int((not a and b) or (a and not b))
    carry = int(a and b)
    return sum, carry

def fulladder(a, b, c):
    sum1, carry1 = halfadder(a, b)
    sum2, carry2 = halfadder(sum1, c)
    carry = int(carry1 or carry2)
    return sum2, carry

def twos_complement(A):
    A = [int(not bit) for bit in A]
    A = binary_addition(A, [0] * (len(A) - 1) + [1])
    return A

def ones_complement(A):
    A = [int(not bit) for bit in A]
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

def binary_subtraction(A, B):
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    B = twos_complement(B)
    Cin = 0
    S = []
    for i in range(max_len-1, -1, -1):
        sum, Cin = fulladder(A[i], B[i], Cin)
        S.insert(0, sum)
    return S

def ASR(A, B, q_1):
    bit = len(A)
    q_1 = B[-1]
    for i in range(len(B)-1, 0, -1):
        B[i] = B[i-1]

    B[0] = A[-1]
    for i in range(len(A)-1, 0, -1):
        A[i] = A[i-1]

    return A, B, q_1

def booth_multiplication(M, Q):
    bit = len(M)
    A = [0] * bit
    q0 = Q[-1]
    q1 = 0
    print(A)
    for i in range(bit):
        print("Here i=", i, "q0=", q0, "q1=", q1)

        if q0 == 0 and q1 == 1:
            print("Addition")
            A = binary_addition(A, M)
        elif q0 == 1 and q1 == 0:
            print("Subtraction")
            A = binary_subtraction(A, M)

        A, Q, q1 = ASR(A, Q, q1)
        q0 = Q[-1]
        print("Result", A, Q)

    if q1==1:
        A=ones_complement(A)
        Q=twos_complement(Q)

    return A, Q

def take_input():
    num1 = input("Enter multiplicand  :")
    num2 = input("Enter multiplier :")
    A = [int(x) for x in num1]
    B = [int(x) for x in num2]
    return A, B

multiplicand, multiplier = take_input()
a, q = booth_multiplication(multiplicand, multiplier)
print(a, q)

