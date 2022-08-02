R,C,ZR,ZC = map(int,input().split())
printed = []
for _ in range(R):
    scan = input()
    newword = ''
    for sc in scan:
        newword+=sc*ZC
    for zc in range(ZR):
        printed.append(newword)
for pr in printed:
    print(pr)