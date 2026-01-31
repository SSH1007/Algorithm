import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = dict()
    _ = int(input())
    lst = list(map(int, input().split()))
    for l in lst:
        if l not in dic:
            dic[l] = 1
        else:
            dic[l] += 1
    lst2 = sorted(list(dic.items()), key=lambda x: (x[1], -x[0]))
    dap = []
    for l in lst2:
        if l[1] == 1:
            dap.append(l)
    if dap == []:
        print('none')
        return
    else:
        print(lst.index(dap[0][0])+1)


if __name__ == '__main__':
    main()