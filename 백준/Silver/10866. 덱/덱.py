import sys
input = sys.stdin.readline

Deque = []
def push_front(arr,x):
    arr.insert(0,x)

def push_back(arr,x):
    arr.append(x)

def front(arr):
    if len(arr)>0:
        print(arr[0])
    else:
        print(-1)

def back(arr):
    if len(arr)>0:
        print(arr[-1])
    else:
        print(-1)

def size(arr):
    print(len(arr))

def empty(arr):
    if len(arr)>0:
        print(0)
    else:
        print(1)

def pop_front(arr):
    if len(arr) > 0:
        print(arr.pop(0))
    else:
        print(-1)

def pop_back(arr):
    if len(arr) > 0:
        print(arr.pop())
    else:
        print(-1)

N = int(input())
for _ in range(N):
    inst = input().split()
    if len(inst)<2:
        inst = inst[0]
    if 'push_back' in inst:
        push_back(Deque,int(inst[-1]))
    elif 'push_front' in inst:
        push_front(Deque, int(inst[-1]))
    elif 'front' == inst:
        front(Deque)
    elif 'back' == inst:
        back(Deque)
    elif 'size' == inst:
        size(Deque)
    elif 'empty' == inst:
        empty(Deque)
    elif 'pop_front' == inst:
        pop_front(Deque)
    elif 'pop_back' == inst:
        pop_back(Deque)