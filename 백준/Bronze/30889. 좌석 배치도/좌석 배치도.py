import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    theater = [['.']*20 for _ in range(10)]
    for _ in range(N):
        info = input()
        r = info[0]
        c = info[1:]
        theater[ord(r)-65][int(c)-1] = 'o'
    for t in theater:
        print(''.join(t))


if __name__ == '__main__':
    main()