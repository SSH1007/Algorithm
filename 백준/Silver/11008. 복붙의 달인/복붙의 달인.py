T = int(input())
for _ in range(T):
    s, p = input().split()
    s = s.replace(p, ' ')
    print(len(s))