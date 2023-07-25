b = input()
dic = {'000':'0', '001':'1', '010':'2', '011':'3', '100':'4', '101':'5','110':'6','111':'7'}
while 1:
    if len(b)%3 == 0:
        break
    else:
        b = '0'+b

dap = ''
for i in range(0, len(b), 3):
    dap += dic[b[i:i+3]]
print(dap)