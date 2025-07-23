import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    dic = dict()
    for s in S:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    o_c, e_c = 0, 0
    for i in dic.values():
        if i%2:
            o_c += 1
        else:
            e_c += 1
    if o_c == 0 and e_c > 0:
        print(0)
    elif e_c == 0 and o_c > 0:
        print(1)
    else:
        print(2)


if __name__ == '__main__':
    main()