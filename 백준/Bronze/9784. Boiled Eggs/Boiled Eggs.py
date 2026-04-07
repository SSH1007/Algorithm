import sys
input = lambda: sys.stdin.readline().rstrip()


def quick(lst):
    if len(lst) <= 0:
        return lst
    pivot = lst[len(lst)//2]
    left, mid, right = [], [], []
    for l in lst:
        if l < pivot:
            left.append(l)
        elif l > pivot:
            right.append(l)
        else:
            mid.append(l)
    return quick(left)+mid+quick(right)


def main():
    T = int(input())
    for t in range(1, T+1):
        n, P, Q = map(int, input().split())
        eggs = list(map(int, input().split()))
        tmp = quick(eggs)
        weight = 0
        p = 0
        while 1:
            if p >= len(tmp) or p >= P:
                p -= 1
                break
            weight += tmp[p]
            if weight > Q:
                p -= 1
                break
            p += 1
        print(f'Case {t}: {p+1}')


if __name__ == '__main__':
    main()