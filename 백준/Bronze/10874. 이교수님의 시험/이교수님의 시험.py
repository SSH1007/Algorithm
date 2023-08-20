N = int(input())
answer = []
for n in range(1, N+1):
    lst = list(map(int, input().split()))
    score = 0
    for i in range(1, 11):
        if lst[i-1] == ((i-1)%5+1):
            score += 1
    if score == 10:
        answer.append(n)
for a in answer:
    print(a)