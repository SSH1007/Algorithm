import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    p, m = map(int, input().split())
    lst = []
    for _ in range(p):
        l, n = input().split()
        l = int(l)
        flag = False
        for i in range(len(lst)):
            if lst[i][0]-10 <= l <= lst[i][0]+10 and len(lst[i])-1 < m:
                flag = True
                lst[i].append((l, n))
                break
        if not flag:
            lst.append([l, (l, n)])
    for room in lst:
        info = sorted(room[1:], key=lambda x:x[1])
        if len(info) == m:
            print('Started!')
        else:
            print('Waiting!')
        for i in info:
            print(i[0], i[1])


if __name__ == '__main__':
    main()