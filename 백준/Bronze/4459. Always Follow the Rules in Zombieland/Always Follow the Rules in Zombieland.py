import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    q = int(input())
    lst = []
    for _ in range(q):
        lst.append(input())
    for _ in range(int(input())):
        r = int(input())
        print(f'Rule %d: ' % r, end='')
        if r > q or r < 1:
            print('No such rule')
        else:
            print(lst[r-1])
            

if __name__ == '__main__':
    main()