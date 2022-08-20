import sys
input = sys.stdin.readline

A = input()
B = input()
arr = []
for i in range(8):
    arr.append(int(A[i]) + int(B[i]))
    if i<7:
        arr.append(int(A[i+1]) + int(B[i]))
C = ''.join(map(str,[a%10 for a in arr]))

while len(C)>2:
    tmp = []
    for i in range(len(C)-1):
        tmp.append((int(C[i])+int(C[i+1])))
    C = ''.join(map(str,[t%10 for t in tmp]))
print(C)

