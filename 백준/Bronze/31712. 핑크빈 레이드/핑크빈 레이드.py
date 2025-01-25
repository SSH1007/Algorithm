import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    Cu, Du = map(int, input().split())
    Cd, Dd = map(int, input().split())
    Cp, Dp = map(int, input().split())
    H = int(input())
    sec = 0
    while 1:
        if sec%Cu==0:
            H -= Du
        if sec%Cd==0:
            H -= Dd
        if sec%Cp==0:
            H -= Dp
        if H <= 0:
            break
        sec += 1
    print(sec)


if __name__ == '__main__':
    main()