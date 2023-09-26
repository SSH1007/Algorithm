n = int(input())
a = input()
b = input()
cnt = 0
for i in range(n):
    if a[i] == b[i]:
        cnt += 1
print(cnt)