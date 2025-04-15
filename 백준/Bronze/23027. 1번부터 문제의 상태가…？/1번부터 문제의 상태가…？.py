import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = list(input())
    if 'A' in S:
        for i in range(len(S)):
            if S[i] in ['B','C','D','F']:
                S[i] = 'A'
    elif 'B' in S:
        for i in range(len(S)):
            if S[i] in ['C','D','F']:
                S[i] = 'B'
    elif 'C' in S:
        for i in range(len(S)):
            if S[i] in ['D','F']:
                S[i] = 'C'
    else:
        S = ['A']*len(S)
    print(''.join(S))


if __name__ == '__main__':
    main()