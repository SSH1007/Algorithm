def Tawla(a, b):
    dap = ''
    dic = {1:'Yakk', 2:'Doh', 3:'Seh', 4:'Ghar', 5:'Bang', 6:'Sheesh'}
    if a != b:
        if max(a, b) == 6 and min(a, b) == 5:
            dap = 'Sheesh Beesh'
        else:
            dap = dic[max(a, b)] + ' ' + dic[min(a, b)]
    else:
        if a == 1:
            dap = 'Habb Yakk'
        elif a == 2:
            dap = 'Dobara'
        elif a == 3:
            dap = 'Dousa'
        elif a == 4:
            dap = 'Dorgy'
        elif a == 5:
            dap = 'Dabash'
        elif a == 6:
            dap = 'Dosh'
    return dap


T = int(input())
dap = []
for _ in range(T):
    a, b = map(int, input().split())
    dap.append(Tawla(a, b))
for i in range(1, len(dap)+1):
    print(f'Case {i}: {dap[i-1]}')