dan = input()
lst = []
for i in range(1, len(dan)-1):
    for j in range(i+1, len(dan)):
        a = dan[:i]
        b = dan[i:j]
        c = dan[j:]
        a = ''.join(reversed(a))
        b = ''.join(reversed(b))
        c = ''.join(reversed(c))
        lst.append(a+b+c)
print(sorted(lst)[0])