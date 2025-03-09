import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(N, 2, -1):
        print(f'%d bottles of beer on the wall, %d bottles of beer.' % (n, n))
        print(f'Take one down and pass it around, %d bottles of beer on the wall.' % (n-1))
        print()
    if N>1:
        print('2 bottles of beer on the wall, 2 bottles of beer.')
        print('Take one down and pass it around, 1 bottle of beer on the wall.')
        print()
    print('1 bottle of beer on the wall, 1 bottle of beer.')
    print('Take one down and pass it around, no more bottles of beer on the wall.')
    print()
    print('No more bottles of beer on the wall, no more bottles of beer.')
    if N>1:
        print(f'Go to the store and buy some more, %d bottles of beer on the wall.' % N)
    else:
        print(f'Go to the store and buy some more, %d bottle of beer on the wall.' % N)


if __name__ == '__main__':
    main()