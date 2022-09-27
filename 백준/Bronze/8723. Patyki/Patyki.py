abc = list(map(int, input().split()))
abc.sort(reverse=True)
if abc[0]**2 == abc[1]**2 + abc[2]**2:
    print(1)
elif abc[0]==abc[1]==abc[2]:
    print(2)
else:
    print(0)