import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        P_1 = input()
        if P_1 == 'E':
            break
        P_2 = input()
        win = {'R':'S', 'P':'R', 'S':'P'}
        a, b = 0, 0
        for p1, p2 in zip(P_1, P_2):
            if win[p1] == p2:
                a += 1
            elif win[p2] == p1:
                b += 1
        print(f'P1: {a}')
        print(f'P2: {b}')


if __name__ == '__main__':
    main()