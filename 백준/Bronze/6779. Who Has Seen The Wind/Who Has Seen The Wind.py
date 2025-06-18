import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    h = int(input())
    M = int(input())
    dap = 0
    for t in range(1, M+1):
        A = -6*(t**4) + h*(t**3) + 2*(t**2) + t
        if A <= 0:
            print(f'The balloon first touches ground at hour: {t}')
            break
    else:
        print('The balloon does not touch ground in the given time.')


if __name__ == '__main__':
    main()