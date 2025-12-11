import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and  i != k and j != k:
                    if ((A[i]-A[j])/A[k])%1:
                        print('no')
                        return
    print('yes')


if __name__ == '__main__':
    main()