n = int(input())
q = input()

promise = ['000000', '001111', '010011', '011100',
'100110', '101001', '110101', '111010']

def bimil(n, q):
    okay = ''
    for i in range(n):
        notokay = 0
        tmp = q[6*i:6*(i+1)]
        for p in range(len(promise)):
            cnt = 0
            for t in range(len(tmp)):
                if tmp[t] == promise[p][t]:
                    cnt+=1
            if cnt>=5:
                okay+=chr(p+65)
                break
            else:
                notokay+=1
        if notokay==8:
            return i+1
    return okay

print(bimil(n,q))