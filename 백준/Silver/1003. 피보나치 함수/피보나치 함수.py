import sys
input = sys.stdin.readline

# 0~2까지의 호출 횟수를 미리 배열에 저장
zero = [1,0,1]+[0]*38
one = [0,1,1]+[0]*38

def fibo(n):
    if n>=2: # 미리 저장한 값 이상이 들어오면
        for i in range(2, n+1):
            zero[i]=(zero[i-1]+zero[i-2])# 배열에 호출횟수를 피보나치식으로 계산한 값을 append
            one[i]=(one[i-1]+one[i-2])   # 배열에서 불러오면 되므로 중복 호출 필요 없음
    print(f'{zero[n]} {one[n]}')         # 피보나치 n에서의 0,1 호출 횟수 = 피보나치 n-1에서의 호출횟수 + 피보나치 n-2에서의 호출횟수

T = int(input())
for _ in range(T):
    N = int(input())
    fibo(N)