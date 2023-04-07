n = 1
Cn = int(input())

while 1:
    if Cn==1:
        break
    if Cn%2:
        Cn = 3*Cn+1
    else:
        Cn = Cn//2
    n+=1
print(n)