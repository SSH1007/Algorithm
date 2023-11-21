S = ''
while 1:
    try:
        S += input()
    except:
        break
Ss = list(map(int, S.split(',')))
print(sum(Ss))