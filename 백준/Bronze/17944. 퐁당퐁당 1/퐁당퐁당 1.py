N, T = map(int, input().split())
maxN, minN = N*2, 1
cnt = 0
flag = True
for _ in range(T):
    if flag:
        cnt += 1
    else:
        cnt -= 1
    if flag and cnt >= maxN:
        flag = False
    elif not flag and cnt <= minN:
        flag = True
print(cnt)