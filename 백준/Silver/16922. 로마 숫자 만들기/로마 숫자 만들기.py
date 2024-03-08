N = int(input())
rome = [1, 5, 10, 50]
numbers = [0]*(50*20+1)


def DFS(count, num, start):
    if count == N:
        numbers[num] = 1
        return
    for i in range(start, 4):
        num += rome[i]
        DFS(count+1, num, i)
        num -= rome[i]


DFS(0, 0, 0)
print(sum(numbers))