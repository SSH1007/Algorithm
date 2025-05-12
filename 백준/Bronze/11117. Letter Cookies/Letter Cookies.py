import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        sDic = dict()
        S = input()
        for s in S:
            if s not in sDic:
                sDic[s] = 1
            else:
                sDic[s] += 1
        W = int(input())
        for _ in range(W):
            iDic = dict()
            I = input()
            for i in I:
                if i not in iDic:
                    iDic[i] = 1
                else:
                    iDic[i] += 1
            flag = True
            for a, c in iDic.items():
                if sDic.get(a):
                    if sDic[a] < c:
                        flag = False
                else:
                    flag = False
            if flag:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    main()