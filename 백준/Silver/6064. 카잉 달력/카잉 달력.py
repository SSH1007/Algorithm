# 예제의 33은 10*?+3이자 12*!+9이다.
# 33-3인 30은 10으로 나누어떨어진다. => (33-3)%10 == 0
# 또한 33-9는 12로 나누어 떨어진다. => (33-9)%12 == 0
# 이를 식으로 만들면 (k-x)%M == 0 and (k-y)%N == 0
# k의 초기값을 x나 y로 하고, M이나 N만큼 증가시키다보면 두 조건을 만족시키는 k가 나온다.
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    # k를 x로 하고 M만큼 증가시켜도 무방
    k = y
    while k <= M*N:
        if (k-x) % M == 0 and (k-y) % N == 0:
            print(k)
            break
        k += N
    else:
        print(-1)