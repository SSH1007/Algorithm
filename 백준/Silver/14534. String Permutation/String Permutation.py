import sys
input = sys.stdin.readline

def dap():
    # 순열 알고리즘. 문자열 리스트, 선택한 문자들 리스트, 문자 사용 여부 표시리스트를 인수로 받는다.
    def perm(lst, stack, used):
        if len(stack) == len(lst):
            print(*stack, sep = '')
            return
        for i in range(len(lst)):
            # 아직 사용을 안한 문자라면
            if not used[i]:
                used[i] = 1
                stack.append(lst[i])
                # 현재 상황을 기준으로 재귀
                perm(lst, stack, used)
                # 원래대로 초기화
                used[i] = 0
                stack.pop()

    N = int(input().rstrip())
    for n in range(N):
        lst = list(input().rstrip())
        stack = []
        used = [0 for _ in range(len(lst))]
        print(f'Case # {1+n}:')
        perm(lst, stack, used)

if __name__ == '__main__':
    dap()