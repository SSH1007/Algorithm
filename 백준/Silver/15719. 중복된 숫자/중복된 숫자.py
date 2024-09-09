import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    Ns = input()
    NumSum = (N-1)*N//2
    nSum = 0
    tmp = ''
    for n in Ns:
        if n.isdigit():
            tmp += n
        else:
            nSum += int(tmp)
            tmp = ''
    nSum += int(tmp)
    print(nSum-NumSum)


if __name__ == '__main__':
    main()