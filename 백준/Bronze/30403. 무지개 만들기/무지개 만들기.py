import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    dic = {'R':0, 'O':1, 'Y':2, 'G':3, 'B':4, 'I':5, 'V':6,
           'r':7, 'o':8, 'y':9, 'g':10, 'b':11, 'i':12, 'v':13}
    lst = [0]*14
    for n in range(N):
        if not dic.get(S[n]) == None:
            if lst[dic[S[n]]] == 0:
                lst[dic[S[n]]] += 1
    A, B = sum(lst[:7]), sum(lst[7:14])
    if A == B == 7:
        print('YeS')
    elif A == 7:
        print('YES')
    elif B == 7:
        print('yes')
    else:
        print('NO!')


if __name__ == '__main__':
    main()