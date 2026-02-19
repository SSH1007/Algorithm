import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu',
           'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']
    N = int(input())-1
    K = N//14
    if N % 14 in [2, 6, 10]:
        print(f'tu+ru*{K+2}' if K >= 3 else 'tururu'+'ru'*K)
    elif N % 14 in [3, 7, 11]:
        print(f'tu+ru*{K+1}' if K >= 4 else 'turu'+'ru'*K)
    else:
        print(lst[N%14])


if __name__ == '__main__':
    main()