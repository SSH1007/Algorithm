dap = 0
while 1:
    try:
        input()
        dap += 1
    except EOFError:
        break
print(dap)