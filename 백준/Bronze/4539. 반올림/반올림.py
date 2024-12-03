n = int(input())
for _ in range(n):
    s = list(map(int, input()))[::-1]
    for i in range(len(s)-1):
        if s[i] > 4:
            s[i+1] += 1
        s[i] = 0
    print(''.join(map(str, s[::-1])))