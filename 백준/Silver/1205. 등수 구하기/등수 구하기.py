N, newRecord, P = map(int, input().split())
if N == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    keeper = score[:N][-1]

    score.append(newRecord)
    score.sort(reverse=True)
    if N >= P:
        if newRecord <= keeper:
            print(-1)
        else:
            print(score[:P].index(newRecord)+1)
    else:
            print(score[:P].index(newRecord)+1)