X = input()
curV = ''
maxV = '999999'
visited = [False]*len(X)


def backTracking(depth):
    global curV
    global maxV
    if depth == len(X):
        if X < curV < maxV:
            maxV = curV
    for i in range(len(X)):
        if not visited[i]:
            curV += X[i]
            visited[i] = True
            backTracking(depth + 1)
            curV = curV[:-1]
            visited[i] = False


backTracking(0)
if maxV == '999999':
    maxV = '0'
print(maxV)