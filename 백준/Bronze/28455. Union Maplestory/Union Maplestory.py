import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    L = [int(input()) for _ in range(N)]
    L.sort(reverse=True)
    lvs = [60,100,140,200,250]
    hap, up = 0, 0
    for l in L[:42]:
        for lv in lvs:
            if l>=lv:
                up += 1
        hap += l
    print(hap, up)


if __name__ == '__main__':
    main()