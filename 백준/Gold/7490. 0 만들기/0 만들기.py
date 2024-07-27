import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        s = set()

        # calc = 0: ' ', 1: '+', -1: '-'
        def rec(current, calc, nextNum, term, stR):
            if term == N:
                # current = 현재까지의 연산값
                current += calc*nextNum
                if current == 0:
                    s.add(stR)
                return
            # nextNum = 다음에 계산할 수
            rec(current,              calc, nextNum*10+(term+1), term+1,  stR+' '+str(term+1))
            rec(current+calc*nextNum, 1,     term+1,             term+1,  stR+'+'+str(term+1))
            rec(current+calc*nextNum, -1,    term+1,             term+1,  stR+'-'+str(term+1))

        # 0부터 시작하여 1~7항을 계산한다
        rec(0, 1, 1, 1, '1')
        for l in sorted(list(s)):
            print(l)
        print()


if __name__ == '__main__':
    main()