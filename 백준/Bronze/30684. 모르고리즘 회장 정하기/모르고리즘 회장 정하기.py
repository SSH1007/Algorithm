import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = []
    N = int(input())
    for _ in range(N):
        name = input()
        if len(name) == 3:
            lst.append(name)
    lst.sort()
    print(lst[0])


if __name__ == '__main__':
    main()