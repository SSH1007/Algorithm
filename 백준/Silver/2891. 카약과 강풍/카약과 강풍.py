import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, S, R = map(int, input().split())
    boat = [1]*N
    Ss = list(map(int, input().split()))
    for s in Ss:
        boat[s-1] -= 1
    Rs = list(map(int, input().split()))
    for r in Rs:
        boat[r-1] += 1
    for n in range(N):
        if boat[n] == 0:
            if n > 0:
                if boat[n-1] == 2:
                    boat[n-1] -= 1
                    boat[n] += 1
                    continue
            if n < N-1:
                if boat[n+1] == 2:
                    boat[n+1] -= 1
                    boat[n] += 1
    print(boat.count(0))


if __name__ == '__main__':
    main()