T = int(input())
for _ in range(T):
    a = input().upper()
    if a == a[::-1]:
        print('Yes')
    else:
        print('No')