import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dic = dict()
    for _ in range(N):
        S = ''.join(sorted(list(input())))
        if S not in dic:
            dic[S] = 1
        else:
            dic[S] += 1
    print(len(dic))


if __name__ == '__main__':
    main()