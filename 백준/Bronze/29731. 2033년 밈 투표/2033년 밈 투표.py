import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = ['Never gonna give you up', 'Never gonna let you down',
           'Never gonna run around and desert you',
           'Never gonna make you cry', 'Never gonna say goodbye',
           'Never gonna tell a lie and hurt you', 'Never gonna stop']
    N = int(input())
    for _ in range(N):
        S = input()
        if S not in lst:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()