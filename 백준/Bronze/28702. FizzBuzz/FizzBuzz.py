import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = 0
    for n in range(3, 0, -1):
        S = input()
        if S not in ['Fizz', 'Buzz', 'FizzBuzz']:
            N = int(S)+n
    if N % 3 == 0 and N % 5 == 0:
        print('FizzBuzz')
    elif N % 3 == 0 and N % 5:
        print('Fizz')
    elif N % 3 and N % 5 == 0:
        print('Buzz')
    else:
        print(N)


if __name__ == '__main__':
    main()