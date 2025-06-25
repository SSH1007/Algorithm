import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        bit = input()
        dap = 0
        for i in range(0, len(bit), 8):
            if bit[i:i+8].count('1') % 2 != 0:
                dap += 1
        print(dap)


if __name__ == '__main__':
    main()