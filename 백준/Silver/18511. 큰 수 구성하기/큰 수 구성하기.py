import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    Ks = list(map(str, input().split()))
    lst_ = []

    for l in range(1, len(str(N))+1):
        for a in Ks:
            stack = [[a]]
            while stack:
                top = stack.pop()
                if len(top) == l:
                    lst_.append(int(''.join(top)))
                else:
                    for k in Ks:
                        stack.append(top+[k])
    lst_.sort(reverse=True)
    for l in lst_:
        if N >= l:
            print(l)
            break


if __name__ == '__main__':
    main()