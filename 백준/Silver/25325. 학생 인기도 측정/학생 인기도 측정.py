
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    As = list(input().split())
    dic = dict()
    for a in As:
        dic[a] = 0
    for _ in range(n):
        lst = list(input().split())
        for l in lst:
            dic[l] += 1
    item = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    for name, score in item:
        print(name, score)


if __name__ == '__main__':
    main()