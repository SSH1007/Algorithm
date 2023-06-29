import sys
input = sys.stdin.readline
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)
Result = []
for q in range(int(input())):
    L = list(map(int, input().rstrip().split()))
    b = 0
    for i in range(1,len(L)):
        if L[i] > (sum(L)-L[0])/L[0]:
            b += 1
        else:
            pass
    Result.append("{:.3f}%".format(roundTraditional(((b/L[0])*100), 3)))
for j in Result:
    print(j)