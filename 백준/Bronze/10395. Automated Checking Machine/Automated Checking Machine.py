A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = len(A)
for i in range(l):
    if A[i] == B[i]:
        print('N')
        break
else:
    print('Y')