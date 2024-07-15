import sys
input = lambda: sys.stdin.readline().rstrip()
# N이 80,000이므로 O(N^2)보다 작아야 함

def main():
    N = int(input())
    dap = 0
    stack = []
    for _ in range(N):
        h = int(input())
        if stack and stack[-1] <= h:
            while stack and stack[-1] <= h:
                stack.pop()
        dap += len(stack)
        stack.append(h)
    print(dap)


if __name__ == '__main__':
    main()