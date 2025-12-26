import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    left = {'q', 'w', 'e', 'r', 't', 'y', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
    T = input()
    L, R, S = 0, 0, 0
    for t in T:
        if t == ' ':
            S += 1
        else:
            if t.isupper():
                S += 1
                t = chr(ord(t)+32)
            if t in left:
                L += 1
            else:
                R += 1
    while S > 0:
        S -= 1
        if L > R:
            R += 1
        else:
            L += 1
    print(L, R)


if __name__ == '__main__':
    main()