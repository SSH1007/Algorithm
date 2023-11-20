while 1:
    n = int(input())
    if n == 0:
        break
    lst = []
    for _ in range(n):
        a = input()
        lst.append((a, a.upper()))
    lst.sort(key=lambda k: k[1])
    print(lst[0][0])