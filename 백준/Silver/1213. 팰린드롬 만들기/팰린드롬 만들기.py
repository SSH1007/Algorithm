dic = dict()
name = input()
for n in name:
    if not n in dic:
        dic[n] = 1
    else:
        dic[n] += 1

even1, even2, odd = [],[],[]
for k, v in dic.items():
    if v%2:
        even1.append(k*(v//2))
        even2.append(k*(v//2))
        odd.append(k)
    else:
        even1.append(k*(v//2))
        even2.append(k*(v//2))

dap = ''.join(sorted(even1)) + ''.join(odd) + ''.join(sorted(even2, reverse=True))
if dap == dap[::-1]:
    print(dap)
else:
    print("I'm Sorry Hansoo")