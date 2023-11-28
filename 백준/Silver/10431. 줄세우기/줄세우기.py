P = int(input())
for p in range(1, P+1):
    cnt = 0
    lst = list(map(int, input().split()))[1:]
    end = len(lst) - 1
    while end > 0:
        last_swap = 0
        for j in range(end):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                cnt += 1
                last_swap = j
        end = last_swap
    print(p, cnt)