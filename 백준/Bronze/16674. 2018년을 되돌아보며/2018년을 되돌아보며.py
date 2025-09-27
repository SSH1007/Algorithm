import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = input()
    for i in [3,4,5,6,7,9]:
        if str(i) in N:
            print(0)
            return
    if '2' in N and '0' in N and '1' in N and '8' in N:
        if N.count('2') == N.count('0') == N.count('1') == N.count('8'):
            print(8)
        else:
            print(2)
    else:
        print(1)


if __name__ == '__main__':
    main()