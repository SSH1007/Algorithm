import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T, W = map(int, input().split())
    # 0초에는 자두를 못받음 > 초기 배열 설정
    tree = [0]
    for _ in range(T):
        tree.append(int(input()))

    # dp[t][w] = t초까지 w번 이동하여 받은 자두의 최대 개수
    dp = [[0]*(W+1) for _ in range(T+1)]
    # 1초까지 움직이지 않았다면 1번 자두나무에 위치 (짝수번 이동)
    # 입력값이 2면 0개, 1이면 1개
    dp[1][0] = tree[1] % 2
    # 반대로 1번 움직였다면 2번 자두나무에 위치 (홀수번 이동)
    # 입력값이 2면 1개, 1이면 0개
    dp[1][1] = tree[1] // 2

    for t in range(2, T+1):
        for w in range(W+1):
            # dp[t][w]는 t-1초까지 w번까지 움직인 결과로 받은 자두의 수의 최대값 "+"
            # t초에 w번 움직인 것으로 받을 수 있는 자두의 수
            dp[t][w] = max(dp[t-1][:w+1])

            # 상기했듯이 움직인 횟수 w가 홀수면 2번 자두나무, 짝수면 1번 자두나무에 위치
            # w번 움직여 위치하게 된 나무(tree[t])에서 자두가 떨어지느냐의 여부 판단
            t_plum = tree[t] // 2 if w % 2 else tree[t] % 2

            dp[t][w] += t_plum

    # W번을 꽉 채워서 이동하는것이 최대값을 보장하지 않으므로
    print(max(dp[T]))


if __name__ == '__main__':
    main()