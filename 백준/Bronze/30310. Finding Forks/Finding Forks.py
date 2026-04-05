import sys
input = lambda: sys.stdin.readline().rstrip()


def quick(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]
    fro, mid, bac = [], [], []
    for l in lst:
        if l < pivot:
            fro.append(l)
        elif l == pivot:
            mid.append(l)
        else:
            bac.append(l)
    return quick(fro) + mid + quick(bac)


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    dap = quick(a)
    print(sum(dap[:2]))


if __name__ == '__main__':
    main()