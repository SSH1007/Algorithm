T = int(input())
for _ in range(T):
    letter = input()
    l = int(len(letter)**0.5)
    for i in range(1, l+1):
        for j in range(1, l+1):
            print(letter[l*j-i], end='')
    print()