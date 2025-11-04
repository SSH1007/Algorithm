import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    lst = [0]*26
    for s in S:
        o = ord(s)
        if 65 <= o <= 90:
            lst[o-65] += 1
        elif 97 <= o <= 122:
            lst[o-97] += 1
    for i in range(26):
        print(f'{chr(i+65)} | {"*"*lst[i]}')


if __name__ == '__main__':
    main()