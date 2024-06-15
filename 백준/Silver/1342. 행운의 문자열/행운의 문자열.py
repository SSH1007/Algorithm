def main():
    S = input()
    visited = [0]*len(S)
    s = set()

    def DFS(lst):
        if len(lst) == len(S):
            s.add(''.join(lst))
            return
        for i in range(len(S)):
            if not visited[i]:
                if lst:
                    if S[i] == lst[-1]:
                        continue
                visited[i] = 1
                lst.append(S[i])
                DFS(lst)
                lst.pop()
                visited[i] = 0
        return

    DFS([])
    print(len(s))


if __name__ == '__main__':
    main()