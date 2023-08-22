R, C = map(int, input().split())
A, B = map(int, input().split())
black = True
for r in range(R):
    for a in range(A):
        if r%2:
            for c in range(C):
                if c % 2:
                    print(B*'X', end='')
                else:
                    print(B*'.', end='')
        else:
            for c in range(C):
                if c % 2:
                    print(B*'.', end='')
                else:
                    print(B*'X', end='')
        print()