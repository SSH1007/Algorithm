line = input()
dic = dict()
for l in line:
    if not l in dic:
        dic[l] = 1
    else:
        dic[l] += 1
lst = list(dic.values())
a = lst[0]
odd = True
if a%2 == 0:
    odd = False
for l in lst:
    if (odd and l % 2 == 0) or (not odd and l % 2):
        print('0/1')
        break
else:
    if odd:
        print(1)
    else:
        print(0)