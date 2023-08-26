N = int(input())
i = 10
while i < 10**len(str(N)):
    if int(str(N%i)[0]) > 4:
        N += i
    N -= N % i
    i *= 10
print(N)