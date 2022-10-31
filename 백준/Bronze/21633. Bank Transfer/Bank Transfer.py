k = int(input())
dap = k*0.01+25
if dap < 100:
    print("{:.2f}".format(100))
elif dap > 2000:
    print("{:.2f}".format(2000))
else:
    print("{:.2f}".format(dap))