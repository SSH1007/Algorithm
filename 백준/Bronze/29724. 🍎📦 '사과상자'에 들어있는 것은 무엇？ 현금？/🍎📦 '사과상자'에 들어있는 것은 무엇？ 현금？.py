import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    g, c = 0, 0
    for _ in range(N):
        T, W, H, L = input().split()
        w, h, l = int(W), int(H), int(L)
        if T == 'A':
            n = (w//12)*(h//12)*(l//12)
            g += (n*500+1000)
            c += n*4000
        else:
            g += 6000
    print(g, c, sep='\n')


if __name__ == '__main__':
    main()