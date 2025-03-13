import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    red, blue = 0, 0
    lst = []
    for n in range(8):
        rec, team = input().split()
        lst.append((rec, team))
    lst.sort()
    score = [10,8,6,5,4,3,2,1]
    for i in range(8):
        if lst[i][1] == 'B':
            blue += score[i]
        else:
            red += score[i]
    print('Blue' if blue > red else 'Red')


if __name__ == '__main__':
    main()