import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    mixed = list(input())

    # 예외조건
    if mixed[0] != 'q' or mixed[-1] != 'k' or len(mixed)%5:
        print(-1)
        exit()

    dap = 0
    quack = 'quack'
    # 일단 최대한 돌리고 조건 따져서 종료
    for _ in range(len(mixed)//5):

        idx = 0
        for i in range(len(mixed)):
            if mixed[i] == quack[idx]:
                idx += 1
                if mixed[i] == 'k':
                    idx = 0
                mixed[i] = '_'
        dap += 1
        if mixed.count('_') == len(mixed):
            break
    if mixed.count('_') == len(mixed):
        print(dap)
    else:
        print(-1)


if __name__ == '__main__':
    main()