N = int(input())
for _ in range(N):
    dicA = {4: 0, 3: 0, 2: 0, 1: 0}
    dicB = {4: 0, 3: 0, 2: 0, 1: 0}
    Alst = list(map(int, input().split()))
    Blst = list(map(int, input().split()))
    for a in Alst[1:]:
        dicA[a] += 1
    for b in Blst[1:]:
        dicB[b] += 1

    for i in range(4,0,-1):
        if dicA[i] > dicB[i]:
            print('A')
            break
        elif dicA[i] < dicB[i]:
            print('B')
            break
    else:
        print('D')