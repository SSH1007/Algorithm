import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    hl, hh = map(int, input().split())
    sl, sh = map(int, input().split())
    vl, vh = map(int, input().split())
    R, G, B = map(int, input().split())
    M, m = max(R, G, B), min(R, G, B)
    V = M
    S = 255*(V-m)/V
    H = 0
    if V == R:
        H = (60*(G-B))/(V-m)
    elif V == G:
        H = 120 + (60*(B-R))/(V-m)
    else:
        H = 240 + (60*(R-G))/(V-m)
    if H < 0:
        H += 360
    if hl <= H <= hh and sl <= S <= sh and vl <= V <= vh:
        print('Lumi will like it.')
    else:
        print('Lumi will not like it.')


if __name__ == '__main__':
    main()