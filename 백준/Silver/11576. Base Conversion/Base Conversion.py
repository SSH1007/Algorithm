import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
m = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))[::-1]
tmp = 0
# A진법으로 나타낸 수를 10진수로 바꾸기
for i in range(m):
    tmp += lst[i]*(A**i)

# 10진수를 B진법으로 변환하기
def convert(num, zin):
    m , n = divmod(num, zin)
    if m == 0:
        return str(n)
    else:
        return convert(m, zin) + ' ' + str(n)

print(convert(tmp, B))