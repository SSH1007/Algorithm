import sys
input = sys.stdin.readline

N = int(input())
lst = [[0,[]] for _ in range(N+1)]
# 연산 횟수
lst[1][0] = 0
# N을 1로 만드는 방법에 포함되어 있는 수
lst[1][1] = [1]

for n in range(2,N+1):
    lst[n][0] = lst[n-1][0]+1
    lst[n][1] = lst[n-1][1]+[n]    

    if n%3==0 and lst[n][0]>lst[n//3][0]+1:
        lst[n][0] = lst[n//3][0]+1
        lst[n][1] = lst[n//3][1]+[n]
    if n%2==0 and lst[n][0]>lst[n//2][0]+1:
        lst[n][0] = lst[n//2][0]+1
        lst[n][1] = lst[n//2][1]+[n]

print(lst[N][0])
print(*lst[N][1][::-1])