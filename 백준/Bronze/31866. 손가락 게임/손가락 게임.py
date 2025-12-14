import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    j, y = map(int, input().split())
    win = {0: 2, 2: 5, 5: 0}
    if j == y:
        print('=')
        return
    elif win.get(j) != None and win.get(y) == None:
        print('>')
    elif win.get(j) == None and win.get(y) != None:
        print('<')
    elif win.get(j) == None and win.get(y) == None:
        print('=')
    elif win.get(j) == y:
        print('>')
    else:
        print('<')


if __name__ == '__main__':
    main()