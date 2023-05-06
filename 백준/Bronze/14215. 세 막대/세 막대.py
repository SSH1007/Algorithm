abc = sorted(list(map(int, input().split())))
if abc[0]+abc[1] > abc[2]:
    print(sum(abc))
else:
    print(2*(abc[0]+abc[1])-1)