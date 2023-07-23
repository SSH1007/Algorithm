N, K = map(int, input().split())
lst = []
for k in range(1, K+1):
    tmp = N*k
    tmp2 = int(str(tmp)[::-1])
    lst.append(tmp2)
lst.sort(reverse=True)
print(lst[0])