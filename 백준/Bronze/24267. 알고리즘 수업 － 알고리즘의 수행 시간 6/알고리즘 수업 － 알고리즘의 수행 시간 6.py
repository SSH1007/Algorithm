n = int(input())

def MenOfPassion(n):
    lst = [0]*(n)
    tmp = 1
    for i in range(2, n):
        lst[i] = lst[i-1]+tmp
        tmp+=1

    return lst

print(sum(MenOfPassion(n)))
print(3)