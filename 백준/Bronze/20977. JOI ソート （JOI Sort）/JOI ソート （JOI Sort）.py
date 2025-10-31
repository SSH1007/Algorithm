import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    S = input()
    j, o, i = 0, 0, 0
    for s in S:
        if s == 'J': j+=1
        elif s == 'O': o+=1
        else: i+=1
    print('J'*j+'O'*o+'I'*i)


if __name__ == '__main__':
    main()