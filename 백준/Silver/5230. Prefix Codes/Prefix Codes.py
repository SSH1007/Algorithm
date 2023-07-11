T = int(input())
for _ in range(T):
    Q = list(input().split())
    K = Q[0]
    S = Q[1]
    Commands = Q[2:]
    daps = []
    for Command in Commands:
        dap = ''
        idx = 0
        Cs = len(Command)
        for c in range(Cs):
            if Command[c] == '0':
                idx = 2*idx+1
            elif Command[c] == '1':
                idx = 2*idx+2
            if S[idx] != '*':
                dap += S[idx]
                idx = 0
        daps.append(dap)
    print(*daps)