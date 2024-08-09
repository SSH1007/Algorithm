import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = lst.count(0)

    robots = [False]*(2*N)
    s, e = 0, N-1
    dap = 0

    while cnt < K:
        # 1. 벨트 회전
        s = (s-1) % (2*N)
        e = (e-1) % (2*N)

        # 2. 로봇 내리기
        if robots[e]:
            robots[e] = False

        # 3. 로봇 이동
        for i in range(N-2, -1, -1):
            cur = (s+i) % (2*N)
            next = (cur+1) % (2*N)
            if robots[cur] and not robots[next] and lst[next] > 0:
                robots[cur] = False
                robots[next] = True
                lst[next] -= 1
                if lst[next] == 0:
                    cnt += 1

        # 4. 로봇 이동 뒤 내리기
        if robots[e]:
            robots[e] = False

        # 5. 로봇 올리기
        if lst[s] > 0:
            robots[s] = True
            lst[s] -= 1
            if lst[s] == 0:
                cnt += 1

        dap += 1
    print(dap)


if __name__ == '__main__':
    main()