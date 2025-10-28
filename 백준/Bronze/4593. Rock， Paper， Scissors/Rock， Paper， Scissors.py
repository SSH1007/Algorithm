import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = []
    while 1:
        S = input()
        lst.append(S)
        if len(lst)>1:
            if lst[-1] == 'E' and S == 'E':
                break
    for i in range(len(lst)//2):
        N = len(lst[2*i])
        a, b = 0, 0
        for n in range(N):
            if lst[2*i][n] == 'R' and lst[2*i+1][n] == 'S':
                a += 1
            elif lst[2*i][n] == 'R' and lst[2*i+1][n] == 'P':
                b += 1
            elif lst[2*i][n] == 'S' and lst[2*i+1][n] == 'P':
                a += 1
            elif lst[2*i][n] == 'S' and lst[2*i+1][n] == 'R':
                b += 1
            elif lst[2*i][n] == 'P' and lst[2*i+1][n] == 'R':
                a += 1
            elif lst[2*i][n] == 'P' and lst[2*i+1][n] == 'S':
                b += 1
        print(f'P1: {a}')
        print(f'P2: {b}')


if __name__ == '__main__':
    main()