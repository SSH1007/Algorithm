import sys
input = lambda: sys.stdin.readline().rstrip()
# N이 80,000이므로 O(N^2)보다 작아야 함

def main():
    N = int(input())
    dap = 0
    # 각 관리인이 오른쪽만을 바라볼 수 있고,
    # 자신보다 높거나 같은 빌딩이 등장하기 전까지의 빌딩들만 볼 수 있음
    # > 내림차순으로 정렬되도록 스택을 구성하자
    stack = []
    for _ in range(N):
        cur = int(input())
        while stack and stack[-1] <= cur:
            # 현재 빌딩보다 같거나 낮은 빌딩들은 pop해준다
            stack.pop()
        # 현 상태의 스택이 현재 빌딩을 내려다볼 수 있는 빌딩들의 목록
        # print(stack)
        dap += len(stack)
        stack.append(cur)
    print(dap)


if __name__ == '__main__':
    main()