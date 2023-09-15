P = int(input())
s, e, a, n = 0, 0, 0, 0
for _ in range(P):
    Gp, Cp, Np = map(int, input().split())
    if Gp == 1:
        n += 1
    elif Cp == 1 or Cp == 2:
        s += 1
    elif Cp == 3:
        e += 1
    elif Cp == 4:
        a += 1
print(s, e, a, n, sep='\n')