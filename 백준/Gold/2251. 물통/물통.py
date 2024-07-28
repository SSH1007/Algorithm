import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    A, B, C = map(int, input().split())

    # 0, 0, C로 시작하므로 세 물통 안의 물의 양의 합은 언제나 C 물통의 용량과 같다.
    # a+b+c = C
    # a, b만 알면 c는 C-(a+b)라는 것을 알 수 있음.
    # 방문 체크를 2차로 바꾸자(3차의 경우 메모리 97764KB)
    # visited[a][b] = a, b 방문 여부
    visited = [[0]*(B+1) for _ in range(A+1)]
    visited[0][0] = 1
    q = deque([(0, 0)])
    dap = []

    def pour(a, b):
        if not visited[a][b]:
            q.append((a, b))
            visited[a][b] = 1

    while q:
        a, b = q.popleft()
        # a,b,c의 물의 양의 총합은 C의 용량
        c = C-(a+b)

        # A 물통이 비어 있을 때 C 물통 안의 물의 양 체크
        if a == 0:
            dap.append(c)

        # a > b
        # A 물통 안의 a만큼의 물이 비거나,
        # B물통의 (B-b)만큼의 여유분만큼 물을 넣을 수 있음(이하 동일)
        water = min(a, B-b)
        pour(a-water, b+water)
        # a > c
        water = min(a, C-c)
        pour(a-water, b)

        # b > a
        water = min(b, A-a)
        pour(a+water, b-water)
        # b > c
        water = min(b, C-c)
        pour(a, b-water)

        # c > a
        water = min(c, A-a)
        pour(a+water, b)
        # c > b
        water = min(c, B-b)
        pour(a, b+water)
    print(*sorted(dap))


if __name__ == '__main__':
    main()