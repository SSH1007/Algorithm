import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = list(input().split())
    for s in S:
        for n in ['social', 'history', 'language', 'literacy']:
            if n in s:
                print('digital humanities')
                exit(0)
        for n in ['bigdata', 'public', 'society']:
            if n in s:
                print('public bigdata')
                exit(0)


if __name__ == '__main__':
    main()