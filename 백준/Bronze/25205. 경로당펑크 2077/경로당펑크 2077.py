import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = ['r','s','e','f','a','q','t','d','w','c','z','x','v','g']
    N = int(input())
    S = input()
    if S[-1] in lst:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()