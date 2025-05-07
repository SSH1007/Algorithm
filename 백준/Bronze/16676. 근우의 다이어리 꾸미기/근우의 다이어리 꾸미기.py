import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    std, dap = 11, 1
    N = int(input())
    while 1:
        if N < std:
            print(dap)
            break
        else:
            std = std*10+1
            dap += 1
            

if __name__ == '__main__':
    main()