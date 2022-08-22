arr = []
while 1:
    n = input()
    if n =='END':
        break
    emp = ''
    for i in range(len(n)-1,-1,-1):
        emp = emp + n[i]
    arr.append(emp)
for a in arr:
    print(a)