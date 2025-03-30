import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    lst = []
    for n in range(N):
        if S[n] not in ['J', 'A', 'V']:
            lst.append(S[n])
    if len(lst):
        print(''.join(lst))
    else:
        print('nojava')


if __name__ == '__main__':
    main()