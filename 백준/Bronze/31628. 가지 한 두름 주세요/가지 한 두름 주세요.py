import sys
input = sys.stdin.readline
gaji = [list(input().rstrip().split()) for _ in range(10)]
rotated_gaji = list(map(list, zip(*gaji)))


def kiwi():
    for i in range(10):
        if len(set(gaji[i])) == 1:
            return 1
        if len(set(rotated_gaji[i])) == 1:
            return 1


if kiwi():
    print(1)
else:
    print(0)