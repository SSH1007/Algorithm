import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = lst.count(0)
    q = deque(lst)
    robots = deque()
    dap = 0
    while cnt < K:
        q.rotate(1)
        for _ in range(len(robots)):
            robot = robots.popleft()
            robot += 1
            if robot != N-1:
                robots.append(robot)

        for i in range(len(robots)):
            robot = robots.popleft()
            if (robot+1)%(N*2) not in robots and q[(robot+1)%(N*2)] >= 1:
                robot += 1
                robot %= (N*2)
                q[robot] -= 1
                if q[robot] == 0:
                    cnt += 1
                if robot != N-1:
                    robots.append(robot)
            else:
                robots.append(robot)

        if q[0] > 0:
            robots.append(0)
            q[0] -= 1
            if q[0] == 0:
                cnt += 1
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()