tmp = []
visited = [0]*10
dap = 0
score = list(map(int, input().split()))


def check(lst):
    ans = 0
    for i in range(10):
        if score[i] == lst[i]:
            ans += 1
    return ans


def Back(depth):
    global dap
    if len(tmp) >= 3 and tmp[-1] == tmp[-2] == tmp[-3]:
        return
    if depth == 10:
        res = check(tmp)
        if res >= 5:
            dap += 1
        return
    for i in range(1, 6):
        if not visited[depth]:
            visited[depth] = 1
            tmp.append(i)
            Back(depth + 1)
            visited[depth] = 0
            tmp.pop()


Back(0)
print(dap)