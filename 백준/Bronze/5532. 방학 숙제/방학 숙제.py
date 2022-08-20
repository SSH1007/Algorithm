from math import ceil
arr = []
for _ in range(5):
    arr.append(int(input()))
L,A,B,C,D = arr
print(L -max(ceil(A/C), ceil(B/D)))
