B = int(input())
kpa = B*5-400
print(kpa)
if kpa > 100:
    print(-1)
elif kpa < 100:
    print(1)
else:
    print(0)