import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    std = input()
    N = int(input())
    lst = []
    for _ in range(N):
        cpr = input()
        flag = True
        for i in range(9):
            if std[i] != '*' and std[i] != cpr[i]:
                flag = False
                break
        if flag:
            lst.append(cpr)
    print(len(lst))
    for l in lst:
        print(l)


if __name__ == '__main__':
    main()