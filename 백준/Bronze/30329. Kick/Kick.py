import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    dap = 0
    for i in range(len(S)-3):
        if S[i:i+4] == 'kick':
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()