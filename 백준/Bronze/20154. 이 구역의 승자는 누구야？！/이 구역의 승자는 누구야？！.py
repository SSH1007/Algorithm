import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    l = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
    K = input()
    d = 0
    for k in K:
        d += l[ord(k)-65]
    print("I'm a winner!" if d%2 else "You're the winner?")


if __name__ == '__main__':
    main()