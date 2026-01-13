import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {}
    lst = input().split()
    for l in lst:
        if l[0] not in dic:
            dic[l[0]] = 1
        else:
            dic[l[0]] += 1
    print(max(list(dic.values())))


if __name__ == '__main__':
    main()