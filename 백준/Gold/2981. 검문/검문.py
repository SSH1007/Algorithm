# a를 m으로 나눈 나머지와 b를 m으로 나눈 나머지가 같다면, (a-b)는 m의 배수다.
N = int(input())
lst = [0] * N
cha = [0] * (N - 1)
for n in range(N):
    num = int(input())
    lst[n] = num
lst.sort(reverse=True)
for i in range(N - 1):
    cha[i] = lst[i] - lst[i + 1]


# 유클리드 호제법을 통한 최대공약수 함수
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# N개의 수들의 차의 최대 공약수를 구한다.
gcd = cha[0]
for c in range(1, N-1):
    gcd = GCD(gcd, cha[c])

# 중복 제거를 위해 set으로 dap 선언
dap = set()
# 1보다 커야하므로 2에서부터 시작
# 최악의 경우 1000000000까지 돌아봐야하기 때문에 제곱근을 사용하여 단축
for i in range(2, int(gcd**0.5)+1):
    if gcd % i == 0:
        dap.add(i)
        dap.add(gcd//i)
# 위에서 1을 제외했으므로 1로 나눈 나머지, 즉 본래값을 dap에 마지막으로 넣는다.
dap.add(gcd)
# set을 다시 list로 바꾸고 정렬
answer = sorted(list(dap))
print(*answer)