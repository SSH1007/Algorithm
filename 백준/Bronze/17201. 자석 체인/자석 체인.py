import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = input()
    lst = []
    for i in range(0, N*2, 2):
        lst.append(As[i:i+2])
    if len(set(lst)) == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()