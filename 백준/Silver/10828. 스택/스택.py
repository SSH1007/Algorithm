import sys
input = sys.stdin.readline
def push(arr, x):
    arr.append(x)
    return
def pop(arr):
    if len(arr)<1:
        print(-1)
    else:
        a = arr.pop()
        print(a)
    return
def size(arr):
    print(len(arr))
    return
def empty(arr):
    if len(arr)<1:
        print(1)
    else:
        print(0)
    return
def top(arr):
    if len(arr)<1:
        print(-1)
    else:
        print(arr[-1])
    return
N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    if len(command)>1:
        push(stack,command[1])
    else:
        if command[0] == 'pop':
            pop(stack)
        elif command[0] == 'size':
            size(stack)
        elif command[0] == 'empty':
            empty(stack)
        elif command[0] == 'top':
            top(stack)