K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
longest, shortest = max(lst), 1
while longest >= shortest:
    lines = 0
    mid = (longest+shortest)//2
    for l in lst:
        lines += l//mid
    # print(lines, mid, longest, shortest)
    if lines < N:   # 기준값보다 적으면 더 작은 값으로 쪼개야 한다.
        longest = mid-1
    else:   # N개보다 많이 만드는 것도 N개를 만드는 것에 포함
        shortest = mid+1
print(longest)