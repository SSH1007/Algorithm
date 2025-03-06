import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    names = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
    idx, candidate = 0, 0
    for i in range(9):
        club = list(map(int, input().split()))
        tmp = 0
        for c in club:
            if c > tmp:
                tmp = c
        if candidate < tmp:
            candidate = tmp
            idx = i
    print(names[idx])


if __name__ == '__main__':
    main()