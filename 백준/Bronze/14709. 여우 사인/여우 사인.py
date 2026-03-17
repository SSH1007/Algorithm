import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    fox = []
    for _ in range(N):
        a, b = map(int, input().split())
        fox.append({a, b})
    flag = 0
    for f in fox:
        if 2 in f or 5 in f:
            flag = 1
    if flag:
        print('Woof-meow-tweet-squeek')
    else:
        if {1, 3} in fox and {3, 4} in fox and {1, 4} in fox:
            print('Wa-pa-pa-pa-pa-pa-pow!')
        else:
            print('Woof-meow-tweet-squeek')


if __name__ == '__main__':
    main()