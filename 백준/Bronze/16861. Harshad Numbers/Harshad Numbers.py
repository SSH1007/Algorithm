N = int(input())
for n in range(N, 1000000001):
    if n%sum(map(int, str(n))) == 0:
        print(n)
        break