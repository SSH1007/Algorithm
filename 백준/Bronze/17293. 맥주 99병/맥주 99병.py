import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(N, 0, -1):    
        b = "bottle" if n == 1 else "bottles"
        nb = "bottle" if n-1 == 1 else "bottles"
    
        print(f'{n} {b} of beer on the wall, {n} {b} of beer.')
        print(f'Take one down and pass it around, {n-1} {nb} of beer on the wall.\n' if n > 1 else 
              'Take one down and pass it around, no more bottles of beer on the wall.\n')

    print('No more bottles of beer on the wall, no more bottles of beer.')
    print(f'Go to the store and buy some more, {N} {("bottle" if N == 1 else "bottles")} of beer on the wall.')


if __name__ == '__main__':
    main()