import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        s = set()

        def rec(v, cnt, st):
            if cnt == N:
                if eval(st.replace(' ', '')) == 0:
                    s.add(st)
                return

            v += 1

            rec(v, cnt+1, st+' '+str(v))
            rec(v, cnt+1, st+'+'+str(v))
            rec(v, cnt+1, st+'-'+str(v))

        rec(1, 1, "1")
        if t != 0:
            print()
        for f in sorted(list(s)):
            print(f)


if __name__ == '__main__':
    main()