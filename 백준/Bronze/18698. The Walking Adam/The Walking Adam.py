N = int(input())
for _ in range(N):
    move = input()
    cnt = 0
    for i in range(len(move)):
        if move[i] == 'D':
            break
        cnt += 1
    print(cnt)