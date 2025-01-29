import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    A, B = '', ''
    for a in As:
        A += str(a)
    for b in Bs:
        B += str(b)
    if int(A) >= int(B):
        print(B)
    else:
        print(A)


if __name__ == '__main__':
    main()