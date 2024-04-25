import sys
input = sys.stdin.readline
front, back = input().rstrip(), ''


def pal(S):
    s, e = 0, len(S)-1
    while s <= e:
        if S[s] != S[e]:
            return 0
        s += 1
        e -= 1
    return len(S)


for i in range(len(front)):
    p = pal(front+back)
    if p:
        print(p)
        break
    back = front[i] + back