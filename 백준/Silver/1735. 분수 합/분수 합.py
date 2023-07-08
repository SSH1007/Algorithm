A, B = map(int, input().split())
C, D = map(int, input().split())

def GCD(a, b):
    while b!=0:
        a, b = b, a%b
    return a

son = A*D+B*C
mom = B*D
print(son//GCD(son, mom), mom//GCD(son, mom))