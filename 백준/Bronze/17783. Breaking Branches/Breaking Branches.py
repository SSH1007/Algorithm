import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    if int(input())%2:
        print('Bob')
    else:
        print('Alice')
        print(1)


if __name__ == '__main__':
    main()