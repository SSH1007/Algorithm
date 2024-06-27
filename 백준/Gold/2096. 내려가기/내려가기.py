import sys
input = sys.stdin.readline

# dp+슬라이딩 윈도우로 메모리양을 줄이기
def main():
    N = int(input().rstrip())
    graph = list(map(int, input().rstrip().split()))
    dp1 = graph[:]
    dp2 = graph[:]
    for n in range(1, N):
        a, b, c = map(int, input().rstrip().split())
        dp1 = [a+max(dp1[0], dp1[1]), b+max(dp1), c+max(dp1[1], dp1[2])]
        dp2 = [a+min(dp2[0], dp2[1]), b+min(dp2), c+min(dp2[1], dp2[2])]

    print(max(dp1), min(dp2))


if __name__ == '__main__':
    main()