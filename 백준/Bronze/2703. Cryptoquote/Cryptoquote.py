import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        cipher = input()
        rule = input()
        dap = ""
        for i in range(len(cipher)):
            if cipher[i] == " ":
                dap += " "
            else:
                dap += rule[ord(cipher[i])-65]
        print(dap)


if __name__ == '__main__':
    main()