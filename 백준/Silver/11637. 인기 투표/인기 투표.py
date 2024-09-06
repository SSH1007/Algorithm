import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        lst = []
        people = 0
        max_p = 0
        for num in range(1, n+1):
            a = int(input())
            max_p = max(max_p, a)
            lst.append((a, num))
            people += a
        lst.sort()
        cnt = 0
        for l in lst:
            if l[0] == max_p:
                cnt += 1
        if cnt > 1:
            print('no winner')
        elif lst[-1][0] > people//2:
            print('majority winner', lst[-1][1])
        elif lst[-1][0] <= people//2:
            print('minority winner', lst[-1][1])


if __name__ == '__main__':
    main()