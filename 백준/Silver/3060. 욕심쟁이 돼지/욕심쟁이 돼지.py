import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        pigs = list(map(int, input().split()))
        want = pigs[:]
        day = 1
        while 1:
            if N < sum(pigs):
                break
            for i in range(6):
                want[i] = pigs[(i+1)%6] + pigs[(i-1)%6] + pigs[(i+3)%6]
            for i in range(6):
                pigs[i] += want[i]
            day += 1
        print(day)


if __name__ == '__main__':
    main()