import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    Q = int(input())
    for _ in range(Q):
        S = input()
        tmp = 0
        for i in range(len(S)-2):
            if S[i:i+3] == 'WOW':
               tmp += 1
        print(tmp)


if __name__ == '__main__':
    main()