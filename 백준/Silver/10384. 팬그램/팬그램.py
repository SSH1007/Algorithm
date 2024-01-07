N = int(input())
for n in range(1, N+1):
    dic = {}
    text = input()
    for t in text:
        if t.isalpha():
            t = t.upper()
            if not t in dic:
                dic[t] = 1
            else:
                dic[t] += 1
    minv = 100
    for i in dic.values():
        if minv > i:
            minv = i
    print(f'Case {n}: ', end = '')
    if len(dic) == 26:
        if minv == 3:
            print('Triple pangram!!!')
        elif minv == 2:
            print('Double pangram!!')
        elif minv == 1:
            print('Pangram!')
    else:
        print('Not a pangram')