word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s = list(input().split())
dap = ''
if s[0] in word:
    dap += s[0][0].upper()
for i in s:
    if i not in word:
        dap += i[0].upper()
print(dap)