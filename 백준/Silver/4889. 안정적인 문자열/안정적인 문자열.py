import sys
input = sys.stdin.readline
from collections import deque


def main():
    t = 1
    while 1:
        stack = list(input().rstrip())
        if stack[0] == '-':
            break
        tmp = deque()
        dap = 0
        # {}은 빼주고 남은 놈들 중에서 변환해야 하는 것들을 센다
        while stack:
            a = stack.pop()
            if not tmp:
                tmp.append(a)
            else:
                if tmp[0] == '}' and a == '{':
                    tmp.popleft()
                else:
                    tmp.appendleft(a)

        for i in range(0, len(tmp), 2):
            if tmp[i] == tmp[i+1]:
                dap += 1
            else:
                dap += 2
        print(f'%d. %d' % (t, dap))
        t += 1


if __name__ == '__main__':
    main()