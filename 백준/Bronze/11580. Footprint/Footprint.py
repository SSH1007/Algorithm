import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    s = set()
    N = int(input())
    S = input()
    x, y = 0, 0
    s.add((x, y))
    for n in range(N):
        if S[n] == 'E':
            x += 1
        elif S[n] == 'W':
            x -= 1
        elif S[n] == 'S':
            y += 1
        else:
            y -= 1
        s.add((x, y))
    print(len(s))


if __name__ == '__main__':
    main()