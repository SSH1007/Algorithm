N = int(input())
if N == 1:
    print('*')
else:
    for nn in range(N*2):
        if nn%2:
            for n in range(N):
                print('*' if n%2 else ' ', end='')
            print()
        else:
            for n in range(N):
                print(' ' if n%2 else '*', end='')
            if nn!=(N*2-1):
                print()
