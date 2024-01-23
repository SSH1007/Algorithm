N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]


def change(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            A[i][j] = 1 - A[i][j]


if N < 3 or M < 3:
    if A!= B:
        print(-1)
    else:
        print(0)
else:
    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                change(i, j)
                cnt += 1

    if A == B:
        print(cnt)
    else:
        print(-1)