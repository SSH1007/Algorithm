def fun():
    N = int(input())
    lst = sorted(list(set(map(int, input().split()))))
    print(*lst)

if __name__ == '__main__':
    fun()