X = int(input())
stick = [64]

while 1:
    if sum(stick)==X:
        break
    popstick = stick.pop()
    stick.append(popstick//2)
    stick.append(popstick//2)
    if sum(stick[:len(stick)-1])>=X:
        stick.pop()
print(len(stick))