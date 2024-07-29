import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    kids = list(map(int, input().split()))

    # 예제)
    # 1, 3, 5, 6, 10의 차의 집합 hq
    # hq = [2, 2, 1, 4]
    # k=5: 1, 3, 5, 6, 10 => 0
    # k=4: 1, 3, 5,6, 10 => 1
    # k=3: 1,3, 5,6, 10 => 3
    # k=2: 1,3,5,6, 10 => 5
    # k=1: 1,3,5,6,10 => 9
    # ∴ 가장 큰 값을 계속 빼주면 된다

    cha = []
    for i in range(1, N):
        cha.append(kids[i]-kids[i-1])
    cha.sort()
    for _ in range(K-1):
        cha.pop()
    print(sum(cha))


if __name__ == '__main__':
    main()