import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    G = int(input())
    lst = list(map(int, input().split()))
    lst.append(G)
    print(sorted(lst, reverse=True).index(G)+1)


if __name__ == '__main__':
    main()