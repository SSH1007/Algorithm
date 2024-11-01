import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, A, B = map(int, input().split())
    # 딕셔너리로 거리 저장하는 방식
    inf = float('inf')
    dic = {i: inf for i in range(1, N+1)}
    dic[A] = 0
    maps = [[] for _ in range(N+1)]
    for n in range(1, N+1):
        num, *lst = map(int, input().split())
        maps[n].extend(lst)

    q = deque([A])
    while q:
        cur = q.popleft()
        for idx, next in enumerate(maps[cur]):
            # 첫번째말고는 방향 전환하므로 가중치가 1
            switch_flag = 0 if idx == 0 else 1
            if dic[next] > dic[cur]+switch_flag:
                dic[next] = dic[cur]+switch_flag
                q.append(next)
    if dic[B] == inf:
        print(-1)
    else:
        print(dic[B])


if __name__ == '__main__':
    main()