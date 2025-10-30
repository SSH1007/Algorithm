import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    A, D = map(int, input().split())
    r, c = map(int, input().split())
    if N%2: # 홀수
        if D%2: # 오른쪽
            print('NO...')
        else:
            if r == N and c < M:
                print('YES!')
            else:
                print('NO...')
    else:
        # 짝수
        if D%2: # 오른쪽
            if r == N and c < M:
                print('YES!')
            else:
                print('NO...')
        else: #왼쪽
            print('NO...')


if __name__ == '__main__':
    main()