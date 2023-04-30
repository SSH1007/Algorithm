import sys
input = sys.stdin.readline

def fact(n):
    if n > 1:
        return n*fact(n - 1)
    else:
        return 1

def perm(test, stack, used):
    global cnt
    if len(stack) == len(test[0]):
        cnt += 1
        if cnt == int(test[1]):
            return stack
    for l in range(len(test[0])):
        if not used[l]:
            stack.append(test[0][l])
            used[l] = 1
            dap = perm(test, stack, used)
            if dap:
                return dap
            stack.pop()
            used[l] = 0
    return

while 1:
    cnt = 0
    test = input().rstrip().split()
    if len(test) != 2:
        break
    else:
        # 순열은 nPr. 이번 케이스는 n==r이므로 n!/(n-r)! -> n! 즉 n팩토리얼이 경우의 수
        if fact(len(test[0])) < int(test[1]):
            print(test[0], test[1], '= No permutation')
        else:
            used = [0 for i in range(len(test[0]))]
            print(test[0], test[1], '=', ''.join(perm(test, [], used)))