import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = list(input().split())
    for s in S:
        tmp = ''
        for e in s:
            tmp = tmp + e.lower()
        if tmp in ['social', 'history', 'language', 'literacy']:
            print('digital humanities')
            exit(0)
        elif tmp in ['bigdata', 'public', 'society']:
            print('public bigdata')
            exit(0)


if __name__ == '__main__':
    main()