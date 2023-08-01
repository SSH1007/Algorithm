N = int(input())
lst = []
country = [0]*(N+1)
for _ in range(N):
    cn, sn, s = map(int, input().split())
    lst.append((cn, sn, s))
lst.sort(key=lambda x: -x[2])
cnt = 0
for cn, sn, s in lst:
    if cnt == 3:
        break
    if country[cn] < 2:
        print(cn, sn)
        cnt += 1
    country[cn] += 1