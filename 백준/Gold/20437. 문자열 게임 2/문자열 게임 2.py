import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        W = input()
        K = int(input())
        dic = dict()
        for i in range(len(W)):
            if not W[i] in dic:
                dic[W[i]] = [i]
            else:
                dic[W[i]].append(i)

        l, s = 0, 10001
        for v in dic.values():
            if len(v) >= K:
                for i in range(len(v)-K+1):
                    l = max(l, v[i+K-1]-v[i]+1)
                    s = min(s, v[i+K-1]-v[i]+1)
        if s == 10001 or l == 0:
            print(-1)
        else:
            print(s, l)


if __name__ == '__main__':
    main()