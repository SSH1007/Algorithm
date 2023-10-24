ok = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
Q = input()
for q in Q:
    if q not in ok:
        print('NO')
        break
else:
    print('YES')