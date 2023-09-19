# 2 <= k <= 9
k = int(input())
signs = list(input().split())
visited = [0]*10
lst = []


def check(a, b, c):
    if a == '<':
        return b < c
    elif a == '>':
        return b > c
    return True


def bu(s):
    if len(s) == k+1:
        lst.append(s)
        return
    for i in range(10):
        if not visited[i]:
            if len(s) == 0 or check(signs[len(s)-1], int(s[-1]), i):
                visited[i] = 1
                bu(s+str(i))
                visited[i] = 0


bu('')
print(lst[-1], lst[0], sep='\n')