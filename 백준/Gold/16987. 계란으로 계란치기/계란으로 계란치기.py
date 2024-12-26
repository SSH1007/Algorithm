import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
dap = 0


def back(depth):
    global dap
    if depth == N:
        tmp = 0
        for n in range(N):
            if eggs[n][0] <= 0:
                tmp += 1
        if dap < tmp:
            dap = tmp
        return
    # 손에 든 계란이 깨졌으면 다음 계란으로
    if eggs[depth][0] <= 0:
        back(depth+1)
    else:
        flag = True
        # 다른 계란 순회
        for n in range(N):
            # 자기 자신이나 깨진 계란은 패스
            if depth == n or eggs[n][0] <= 0:
                continue
            flag = False    # 다른 계란 중 깰 수 있는 계란이 있었다
            eggs[depth][0] -= eggs[n][1]
            eggs[n][0] -= eggs[depth][1]
            back(depth+1)
            eggs[depth][0] += eggs[n][1]
            eggs[n][0] += eggs[depth][1]
        # 다른 계란 중 깰 수 있는 계란이 더 이상 없다면 종료
        if flag:
            back(N)


back(0)
print(dap)