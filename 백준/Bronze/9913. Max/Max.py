import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dic = dict()
    for _ in range(N):
        i = int(input())
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    print(sorted(list(dic.items()), key=lambda x:-x[1])[0][1])


if __name__ == '__main__':
    main()