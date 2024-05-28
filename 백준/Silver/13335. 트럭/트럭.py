import sys
input = sys.stdin.readline
from collections import deque


def main():
    # n: 트럭 수, w: 다리의 길이, L: 최대 하중
    n, w, L = map(int, input().rstrip().split())
    trucks = deque(list(map(int, input().rstrip().split())))
    bridge = deque()
    # 0kg를 버티는 다리로 초기화
    for _ in range(w):
        bridge.append(0)
    dap = 0
    while bridge:
        bridge.popleft()
        if trucks:
            # 다가오는 선두의 트럭의 무게와 현재 다리가 버티고 있는 하중이
            # 최대 하중 L보다 적다면, 선두의 트럭은 진입 가능
            if sum(bridge) + trucks[0] <= L:
                bridge.append(trucks.popleft())
            # 아니면 다리에는 0kg의 공기(?)만이 남는다
            else:
                bridge.append(0)
        dap += 1
    print(dap)
    return


if __name__ == '__main__':
    main()