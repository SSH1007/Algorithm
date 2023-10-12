import sys
input = sys.stdin.readline
h, m, s = map(int, input().rstrip().split())
q = int(input().rstrip())
time = h*3600 + m*60 + s
for _ in range(q):
    query = list(map(int, input().rstrip().split()))
    if query[0] == 3:
        print(h, m, s)
    elif query[0] == 1:
        time += query[1] % 86400
        if time > 86400:
            time -= 86400
        h = time//3600
        m = (time % 3600)//60
        s = time % 60
    elif query[0] == 2:
        time -= query[1] % 86400
        if time < 0:
            time += 86400
        h = time//3600
        m = (time % 3600)//60
        s = time % 60