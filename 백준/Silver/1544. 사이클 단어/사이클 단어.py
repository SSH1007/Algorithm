import sys
input = sys.stdin.readline


def main():
    N = int(input().rstrip())
    lst = []
    for _ in range(N):
        a = input().rstrip()
        for i in range(len(a)):
            if a[i:]+a[:i] in lst:
                break
        else:
            lst.append(a)

    print(len(lst))


if __name__ == '__main__':
    main()