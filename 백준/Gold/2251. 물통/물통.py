import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    A, B, C = map(int, input().split())

    q = deque([(0, 0, C)])
    visited = {}
    dap = set()

    while q:
        lst = q.popleft()
        # print(lst)
        if lst in visited:
            continue
        else:
            visited[lst] = 1
        if lst[0] == 0:
            dap.add(lst[2])
        for i in range(3):
            # 물이 들어있다면
            if lst[i]:
                if i == 0:
                    if lst[0]+lst[1] >= B:
                        q.append(((lst[0]+lst[1])-B, B, lst[2]))
                    else:
                        q.append((0, lst[0]+lst[1], lst[2]))
                    if lst[0]+lst[2] >= C:
                        q.append(((lst[0]+lst[2])-C, lst[1], C))
                    else:
                        q.append((0, lst[1], lst[0]+lst[2]))
                elif i == 1:
                    if lst[0]+lst[1] >= A:
                        q.append((A, (lst[0]+lst[1])-A, lst[2]))
                    else:
                        q.append((lst[0]+lst[1], 0, lst[2]))
                    if lst[1]+lst[2] >= C:
                        q.append((lst[0], (lst[1]+lst[2])-C, C))
                    else:
                        q.append((lst[0], 0, lst[1]+lst[2]))
                elif i == 2:
                    if lst[0]+lst[2] >= A:
                        q.append((A, lst[1], (lst[0]+lst[2])-A))
                    else:
                        q.append((lst[0]+lst[2], lst[1], 0))
                    if lst[1]+lst[2] >= B:
                        q.append((lst[0], B, (lst[1]+lst[2])-B))
                    else:
                        q.append((lst[0], lst[1]+lst[2], 0))
    print(*sorted(list(dap)))


if __name__ == '__main__':
    main()