t = int(input())
lst = [0]*69
lst[0] = 1
lst[1] = 1
lst[2] = 2
lst[3] = 4
for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        lst[i] = lst[i-1] + lst[i-2] + lst[i-3] + lst[i-4]
    print(lst[n])