import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def main():
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    heapq.heapify(cards)
    dap = 0
    while cards:
        if len(cards) == 1:
            break
        a, b = heapq.heappop(cards), heapq.heappop(cards)
        dap += (a+b)
        heapq.heappush(cards, (a+b))
    print(dap)


if __name__ == '__main__':
    main()