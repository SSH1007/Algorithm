def main():
    A, B = input().split()
    B = int(B)
    visited = [0]*len(A)
    dap = [-1]
    lst = []

    def DFS(depth):
        if depth == len(A):
            C = int(''.join(lst))
            if len(str(C)) < len(A):
                return
            if C > dap[0] and C < B:
                dap[0] = C
            return
        for i in range(len(A)):
            if not visited[i]:
                visited[i] = 1
                lst.append(A[i])
                DFS(depth+1)
                lst.pop()
                visited[i] = 0
    DFS(0)
    print(dap[0])


if __name__ == '__main__':
    main()