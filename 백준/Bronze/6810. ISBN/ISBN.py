dap = 0
sample = '9780921418'
for _ in range(3):
    a = input()
    sample+=a
for i in range(len(sample)):
    if i%2:
        dap += (int(sample[i])*3)
    else:
        dap += (int(sample[i])*1)
print(f'The 1-3-sum is {dap}')