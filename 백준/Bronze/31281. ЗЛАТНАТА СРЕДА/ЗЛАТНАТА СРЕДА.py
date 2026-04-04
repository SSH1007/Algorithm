import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = list(map(int, input().split()))
    for i in range(3):
        for j in range(i, 3):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print(lst[1])


if __name__ == '__main__':
    main()