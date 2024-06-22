import sys
input = sys.stdin.readline


def main():
    N = int(input().rstrip())
    towers = list(map(int, input().rstrip().split()))
    dap = [0]*N
    stack = []
    # N이 500000이므로 O(N^2)는 안 됨. 스택으로 O(N);
    for i in range(N):
        while stack:
            if stack[-1][0] >= towers[i]:
                dap[i] = stack[-1][1]+1
                break
            else:
                stack.pop()
        stack.append((towers[i], i))
    print(*dap)


if __name__ == '__main__':
    main()