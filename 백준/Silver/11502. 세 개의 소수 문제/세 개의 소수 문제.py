sieve = [1]*1001
l = int(1000**0.5)+1
for i in range(2, l):
    if sieve[i]:
        for j in range(i+i, 1001, i):
            sieve[j] = 0

T = int(input())
for _ in range(T):
    # 골드바흐의 강한 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
    # 조건 : 7<=K<=1000
    K = int(input())-3
    for i in range(2, 1001):
        if sieve[i] and sieve[K-i]:
            print(*sorted([3, i, K-i]))
            break