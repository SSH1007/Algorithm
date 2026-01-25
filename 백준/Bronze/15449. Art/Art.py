import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = sorted(list(map(int, input().split())))
    dap = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                if lst[i]+lst[j] > lst[k]:
                    dap += 1
    print(dap)


if __name__ == '__main__':
    main()