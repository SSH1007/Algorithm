import sys
input = sys.stdin.readline


def to_s(s):
    HH, SS = map(int, s.split(':'))
    return HH*60+SS


S, E, Q = map(to_s, input().rstrip().split())
dic = dict()
while 1:
    try:
        time, name = input().rstrip().split()
        h_t = to_s(time)
        if h_t <= S:
            if name not in dic:
                dic[name] = 1
        if E <= h_t <= Q:
            if name in dic:
                dic[name] -= 1
    except:
        break
dap = 0
for n, s in dic.items():
    if s <= 0:
        dap += 1
print(dap)