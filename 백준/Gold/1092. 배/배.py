import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    crains = sorted(list(map(int, input().split())))
    M = int(input())
    boxes = sorted(list(map(int, input().split())))
    visited = [0]*M

    # 박스를 크레인마다 분배. 분배 안 된 박스는 visited에 0으로 체크
    lst = [[] for _ in range(N)]
    cIdx, bIdx = 0, 0
    while cIdx < N:
        for b in range(bIdx, M):
            if boxes[b] <= crains[cIdx] and not visited[b]:
                lst[cIdx].append(boxes[b])
                visited[b] = 1
            else:
                bIdx = b
                break
        cIdx += 1

    # 가벼운 박스는 무게 제한이 큰 크레인에게 옮길 수 있음
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
        tmp = 0
        for n in range(N):
            tmp += len(lst[n])
        if tmp == 0:
            break
    if sum(visited) == M:
        print(dap)
    # 혹시 남은 박스가 있다면 -1 출력
    else:
        print(-1)


if __name__ == '__main__':
    main()