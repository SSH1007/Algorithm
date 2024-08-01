import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    info = list(map(int, input().split()))
    nu = [0]*N
    nu[0] = info[0]
    for i in range(1, N):
        nu[i] = nu[i-1]+info[i]
    
    dap = 0

    # 1. 벌..벌..통
    for i in range(1, N-1):
        a = nu[-1]-nu[0]-info[i]
        b = nu[-1]-nu[i]
        dap = max(dap, a+b)

    # 2. 통..벌..벌
    for i in range(1, N-1):
        a = nu[-1]-info[-1]-info[i]
        b = nu[i-1]
        dap = max(dap, a+b)

    # 3. 벌..통..벌
    for i in range(1, N-1):
        a = nu[i]-nu[0]
        b = nu[-1]-nu[i-1]-info[-1]
        dap = max(dap, a+b)

    print(dap)
    

if __name__ == '__main__':
    main()