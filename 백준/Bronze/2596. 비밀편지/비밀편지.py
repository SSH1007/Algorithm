n = int(input())
q = input()
ango = {'000000':'A', '001111':'B', '010011': 'C', '011100':'D',
'100110':'E', '101001':'F', '110101':'G', '111010':'H'}
okay = []
def bimil(n, q):
    for i in range(n):
        tmp =q[6*i:6*(i+1)]
        if tmp in ango.keys():
            okay.append(ango[tmp])
        else:
            for a in ango.keys():
                cnt = [0]*6
                for j in range(len(a)):
                    if tmp[j]!=a[j]:
                        cnt[j]=1
                if sum(cnt) == 1:
                    okay.append(ango[a])
                    break
            else:
                okay.append(i)
    return okay
dap = bimil(n, q)
result = []
for d in dap:
    try:
        if d.isalpha():
            result.append(d)
    except:
        print(d+1)
        break
else:
    print(''.join(result))