import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    K = int(input())
    N = int(input())
    for _ in range(N):
        M, N = map(int, input().split())
        left_round = K-max(M, N)
        gap = abs(M-N)
        # M과 N 사이의 gap을 left_round 동안
        # 다 맞추는 것으로 채울 수 있느냐를 판별해야 함
        if M == N:
            print(1)
        elif M > N:
            # 영희가 항상 먼저 던진다 =
            # M>N일 경우, M은 영희가 점수를 얻은 경우 포함이므로 -1.
            if (gap-1)-left_round <= 1:
                print(1)
            else:
                print(0)
        else:
            if gap-left_round <= 1:
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()