humans = list(map(int, input().split()))
apple = list(map(int, input().split()))
for h in humans:
    if apple[0] == h:
        print(humans.index(h)+1)
        break
else:
    print(0)