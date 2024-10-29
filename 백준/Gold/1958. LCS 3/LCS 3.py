import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A = input()
    B = input()
    C = input()
    maps = [[[0]*(len(C)+1) for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    for a in range(1, len(A)+1):
        for b in range(1, len(B)+1):
            for c in range(1, len(C)+1):
                if A[a-1] == B[b-1] and B[b-1] == C[c-1]:
                    maps[a][b][c] = maps[a-1][b-1][c-1] + 1
                else:
                    maps[a][b][c] = max(maps[a-1][b][c], maps[a][b-1][c], maps[a][b][c-1])
    print(maps[len(A)][len(B)][len(C)])


if __name__ == '__main__':
    main()