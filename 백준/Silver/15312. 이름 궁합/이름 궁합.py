alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input()
B = input()
lst = []
for i in range(len(A)):
    lst.append(alpha[ord(A[i])-65])
    lst.append(alpha[ord(B[i])-65])
while len(lst) > 2:
    tmplst = []
    for i in range(len(lst)-1):
        tmplst.append((lst[i]+lst[i+1])%10)
    lst = tmplst
print(''.join(map(str,lst)))