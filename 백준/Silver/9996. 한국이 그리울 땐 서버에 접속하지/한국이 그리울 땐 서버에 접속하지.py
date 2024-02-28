N = int(input())
p1, p2 = input().split('*')
for _ in range(N):
    file = input()
    if len(file) < len(p1)+len(p2):
        print('NE')
    else:
        if p1 == file[:len(p1)] and p2 == file[-len(p2):]:
            print('DA')
        else:
            print('NE')