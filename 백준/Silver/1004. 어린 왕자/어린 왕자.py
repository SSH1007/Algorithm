lst = []
T = int(input())
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, cr = map(int,input().split())
        # 만약 출발점이나 도착점과 행성계의 중점간의 거리가
        # 행성계의 반지름보다 짧다면, 우주선은 반드시 행성계를 이탈한다.
        # 둘 다 짧을 경우, 해당 행성계 안에서만 여행한다.
        # 둘 다 긴 경우, 해당 행성계에 진입조차 하지 않는다.
        s = ((x1-cx)**2+(y1-cy)**2)**0.5
        e = ((x2-cx)**2+(y2-cy)**2)**0.5
        if (s>cr and e<cr) or (s<cr and e>cr):
            cnt+=1
    lst.append(cnt)
for l in lst:
    print(l)
