N = int(input())
for _ in range(N):
    q = input()
    if '+'in q:
        a, b = map(int, q.split('+'))
        print(a+b)
    else:
        print('skipped')