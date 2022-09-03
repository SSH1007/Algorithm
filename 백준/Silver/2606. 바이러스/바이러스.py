computer = int(input())
num_of_set = int(input())
net = [[] for _ in range(computer+1)]
for _ in range(num_of_set):
    a, b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)

visited = [0]*(computer+1)
visited[1] = 1
stack = [1]
while stack:
    com = stack.pop()
    for new_node in net[com]:
        if visited[new_node] == 0:
            stack.append(new_node)
        visited[new_node] = 1

print(visited.count(1)-1)