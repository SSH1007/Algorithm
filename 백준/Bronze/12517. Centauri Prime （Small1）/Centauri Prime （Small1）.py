import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = ['a king', 'a queen', 'nobody']
    for t in range(1, int(input())+1):
        S = input()
        r = 0
        if S[-1] == 'y':
            r = 2
        elif S[-1] in {'a', 'e', 'i', 'o', 'u'}:
            r = 1
        print(f'Case #{t}: {S} is ruled by {lst[r]}.')


if __name__ == '__main__':
    main()