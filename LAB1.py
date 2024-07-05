#ADDITION OF TWO UNSIGNED INTEGER BINARY NUMBER

def halfadder(a,b):
    sum=int((not a and b) or (not b and a))
    carry =int( a and b)
    return sum, carry

def fulladder(a,b,c):
    sum1,carry1=halfadder(a,b)
    sum2,carry2=halfadder(sum1,c)
    carry= int(carry1 or carry2)
    return sum2,carry

def fourbitadder(num1,num2):
    s=[0,0,0,0]
    c=0
    for i in range(3,-1,-1):
        s[i],c=fulladder(num1[i],num2[i],c)
    return s,c

num1=[1,0,0,1]
num2=[1,1,0,0]
sum,carry=fourbitadder(num1,num2)
print(sum)
print(carry)