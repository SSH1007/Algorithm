# lambda 다중 조건은 튜플로
N = int(input())
lst = []
for _ in range(N):
    x,y = map(int, input().split())
    lst.append((x,y))
lst.sort(key=lambda x : (x[1], x[0]))
for l in lst:
    print(*l)