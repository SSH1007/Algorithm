import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = input()
    if N == 'fdsajkl;' or N == 'jkl;fdsa':
        print('in-out')
    elif N == 'asdf;lkj' or N == ';lkjasdf':
        print('out-in')
    elif N == 'asdfjkl;':
        print('stairs')
    elif N == ';lkjfdsa':
        print('reverse')
    else:
        print('molu')


if __name__ == '__main__':
    main()