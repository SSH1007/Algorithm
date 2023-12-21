n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

s = set()
lst = []
visited = [0]*n


def f():
    if len(lst) == k:
        s.add(''.join(map(str, lst)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            lst.append(cards[i])
            f()
            visited[i] = 0
            lst.pop()


f()
print(len(s))