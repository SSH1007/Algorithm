n = int(input())
cnt = 0
for i in range(min(n, 5),0,-1):
    if i < n-i:
        break
    cnt += 1
print(cnt)