import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    C = int(input())
    dap = 0
    for _ in range(C):
        code = input()
        i = 0
        tmp = 0
        while i < len(code):
            if code[i:i+3] == 'for':
                tmp += 1
                i+=3
            elif code[i:i+5] == 'while':
                tmp += 1
                i+=5
            else:
                i+=1
        dap = tmp if dap < tmp else dap
    print(dap)


if __name__ == '__main__':
    main()