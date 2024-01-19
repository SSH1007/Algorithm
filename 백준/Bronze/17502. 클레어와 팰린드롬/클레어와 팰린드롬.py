n = int(input())
txt = list(input())
for i in range(n):
    if txt[i] == '?':
        if txt[n-i-1] != '?':
            txt[i] = txt[n-i-1]
        else:
            txt[i] = 'a'
print(''.join(txt))