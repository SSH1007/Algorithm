N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
end = lst[-1]
dap = []
for i in range(1, end+1):
    if not i in lst:
        dap.append(i)
if dap:
    for d in dap:
        print(d)
else:
    print('good job')