import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':3, 'H':3, 'I':1, 'J':1,
           'K':3, 'L':1, 'M':3, 'N':3, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2,
           'U':1, 'V':1, 'W':2, 'X':2, 'Y':2, 'Z':1}
    S = input()
    l = []
    for s in S:
        l.append(dic[s])
    while len(l) > 1:
        tmp = [0]*(len(l)//2)
        for i in range(len(l)):
            if len(l)%2 and i == len(l)-1:
                tmp.append(l[i])
            else:
                tmp[i//2] = (tmp[i//2]+l[i])%10
        l = tmp
    print("I'm a winner!" if l[0]%2 else "You're the winner?")


if __name__ == '__main__':
    main()