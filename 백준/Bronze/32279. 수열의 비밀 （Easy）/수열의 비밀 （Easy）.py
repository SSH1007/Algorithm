import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    p, q, r, s = map(int, input().split())
    a = int(input())
    lst = [0, a]
    for i in range(2, n+1):
        if i%2:
            lst.append(r*lst[(i-1)//2]+s)
        else:
            lst.append(p*lst[i//2]+q)
    print(sum(lst))


if __name__ == '__main__':
    main()