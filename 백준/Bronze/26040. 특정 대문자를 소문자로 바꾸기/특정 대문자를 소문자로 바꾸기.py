A = input()
B = list(input().split())
C = ''
for a in A:
    if a in B:
        C += a.lower()
    else:
        C += a
print(C)