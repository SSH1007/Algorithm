import re
def sumS(S):
    a = re.findall('\d+', S)
    if a == []:
        return 0
    else:
        return sum(int(i) for i in ''.join(a))

N = int(input())
nums = [input() for _ in range(N)]
nums.sort(key=lambda x:(len(x), sumS(x), x))
print(*nums, sep='\n')