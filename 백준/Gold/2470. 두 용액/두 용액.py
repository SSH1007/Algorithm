import sys
input = sys.stdin.readline


def main():
    N = int(input().rstrip())
    potions = sorted(list(map(int, input().rstrip().split())))
    s, e = 0, N-1
    a_s, a_e = 0, 0
    # 특성값의 최대치 : (10억 + 10억-1)+1
    v = 2000000000
    while s < e:
        Q = potions[s]+potions[e]
        if 0 <= abs(Q) < v:
            v = abs(Q)
            a_s, a_e = s, e
        if Q < 0:
            s += 1
        else:
            e -= 1
    print(potions[a_s], potions[a_e])


if __name__ == '__main__':
    main()