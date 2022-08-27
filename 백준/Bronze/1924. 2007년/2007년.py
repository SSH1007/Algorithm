month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

x, y = map(int,input().split())
dap = 0
for i in range(x-1):
    dap+=month[i]
print(day[(dap+y)%7])