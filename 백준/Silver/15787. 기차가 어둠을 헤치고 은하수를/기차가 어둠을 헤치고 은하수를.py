import sys
input = sys.stdin.readline
from collections import deque


def main():
    N, M = map(int, input().rstrip().split())
    trains = [deque([0]*20) for _ in range(N)]
    for _ in range(M):
        info = list(map(int, input().rstrip().split()))
        command, trainIdx = info[0], info[1]-1
        if len(info) > 2:
            seatNum = info[2]-1
        if command == 1:
            trains[trainIdx][seatNum] = 1
        elif command == 2:
            trains[trainIdx][seatNum] = 0
        elif command == 3:
            trains[trainIdx].rotate(1)
            trains[trainIdx][0] = 0
        else:
            trains[trainIdx].rotate(-1)
            trains[trainIdx][19] = 0

    lst = []
    for t in trains:
        if t not in lst:
            lst.append(t)
    print(len(lst))


if __name__ == '__main__':
    main()