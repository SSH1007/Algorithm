def dap():
    from collections import deque
    cards = deque()
    n = int(input())
    cards = deque([i for i in range(1, n+1)])
    while cards:
        print(cards.popleft(), end = ' ')
        if cards:
            top = cards.popleft()
            cards.append(top)

if __name__ == '__main__':
    dap()