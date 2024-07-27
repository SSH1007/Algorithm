import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    crains = sorted(list(map(int, input().split())))
    M = int(input())
    boxes = sorted(list(map(int, input().split())))
    visited = [0]*M
    # print(boxes)
    lst = [[] for _ in range(N)]
    cIdx, bIdx = 0, 0
    while cIdx < N:
        for b in range(bIdx, M):
            if boxes[b] <= crains[cIdx] and not visited[b]:
                lst[cIdx].append(boxes[b])
                visited[b] = 1
            else:
                bIdx = b
                # print(bIdx)
                break
        cIdx += 1
    # print(lst)
    dap = 0

    while 1:
        dap += 1
        for n in range(N-1, -1, -1):
            if lst[n]:
                lst[n].pop()
            else:
                for m in range(n-1, -1, -1):
                    if lst[m]:
                        lst[m].pop()
                        break
        # print(lst)
        tmp = 0
        for n in range(N):
            tmp += len(lst[n])
        if tmp == 0:
            break
    if sum(visited) == M:
        print(dap)
    else:
        print(-1)


if __name__ == '__main__':
    main()