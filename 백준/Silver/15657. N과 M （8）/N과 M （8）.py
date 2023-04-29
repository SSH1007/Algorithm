def dap():
    # N, M은 1 이상 ~ 8 이하
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    stack = []
    def fun(i):
        if len(stack) == M:
            print(*stack)
            return
        for j in range(i, N):
            stack.append(lst[j])
            fun(j)
            stack.pop()
    fun(0)

if __name__ == '__main__':
    dap()