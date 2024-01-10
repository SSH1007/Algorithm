import re
N = int(input())
lst = []
for _ in range(N):
    tmp = re.split('[^0-9]', input())
    num = [int(t) for t in tmp if t != '']
    lst.extend(num)
print(*sorted(lst), sep='\n')