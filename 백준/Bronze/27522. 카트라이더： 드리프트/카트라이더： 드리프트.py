import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    red, blue = 0, 0
    lst = [[] for _ in range(8)]
    for n in range(8):
        rec, team = input().split()
        M, SS, sss = map(int, rec.split(':'))
        M *= 60*1000
        SS *= 1000
        lst[n].extend((M+SS+sss, team))
    lst.sort()
    score = [10,8,6,5,4,3,2,1]
    for i in range(8):
        if lst[i][1] == 'B':
            blue += score[i]
        else:
            red += score[i]
    if red == blue:
        if lst[0][1] == 'B':
            print('Blue')
        else:
            print('Red')
    else:
        print('Blue' if blue > red else 'Red')


if __name__ == '__main__':
    main()