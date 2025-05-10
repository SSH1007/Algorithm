N = input()
r = N.index('@')
b = N.index('#')
g = N.index('!')
if r < b < g or r > b > g:
    print(abs(r-g)-1)
else:
    print(-1)