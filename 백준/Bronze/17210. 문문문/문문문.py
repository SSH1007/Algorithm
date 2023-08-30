N = int(input())
first = int(input())
if N >= 6:
    print('Love is open door')
else:
    for _ in range(N-1):
        first = abs(first - 1)
        print(first)