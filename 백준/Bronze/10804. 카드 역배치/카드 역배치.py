cards=list(range(1,21))
for _ in range(10):
    a,b=map(int,input().split())
    cards = cards[:a-1]+cards[a-1:b][::-1]+cards[b:]
for c in cards:
    print(c,end=' ')