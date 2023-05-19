import sys
input = sys.stdin.readline
score = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
# x: 전공과목별(학점*과목평점) 합.  y: 학점의 총합
x,y = 0,0
for _ in range(20):
    lst = list(input().rstrip().split())
    if lst[2] == 'P':
        continue
    x+=(score[lst[2]] * float(lst[1]))
    y+=float(lst[1])
print(f'{x/y:.6f}')