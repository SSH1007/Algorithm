import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    def F(S):
        s, e = 0, len(S)-1
        while s <= e:
            if S[s] == S[e]:
                s += 1
                e -= 1
                continue
            if S[s+1] == S[e]:  # 왼쪽 제거
                tmp = S[:s] + S[s+1:]
                if tmp == tmp[::-1]:
                    return 1
            if S[s] == S[e-1]:  # 오른쪽 제거
                tmp = S[:e]+S[e+1:]
                if tmp == tmp[::-1]:
                    return 1
            return 2
        return 0

    T = int(input())
    for _ in range(T):
        S = input()
        print(F(S))


if __name__ == '__main__':
    main()