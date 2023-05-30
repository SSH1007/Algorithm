import sys
input = sys.stdin.readline
N = input().rstrip()
for n in range(len(N)):
    if n!=0:
        print()
    if N[n] == '0':
        print('0000')
        print('0  0')
        print('0  0')
        print('0  0')
        print('0000')
    elif N[n] == '1':
        print('   1')
        print('   1')
        print('   1')
        print('   1')
        print('   1')
    elif N[n] == '2':
        print('2222')
        print('   2')
        print('2222')
        print('2')
        print('2222')
    elif N[n] == '3':
        print('3333')
        print('   3')
        print('3333')
        print('   3')
        print('3333')
    elif N[n] == '4':
        print('4  4')
        print('4  4')
        print('4444')
        print('   4')
        print('   4')
    elif N[n] == '5':
        print('5555')
        print('5')
        print('5555')
        print('   5')
        print('5555')
    elif N[n] == '6':
        print('6666')
        print('6')
        print('6666')
        print('6  6')
        print('6666')
    elif N[n] == '7':
        print('7777')
        print('   7')
        print('   7')
        print('   7')
        print('   7')
    elif N[n] == '8':
        print('8888')
        print('8  8')
        print('8888')
        print('8  8')
        print('8888')
    elif N[n] == '9':
        print('9999')
        print('9  9')
        print('9999')
        print('   9')
        print('   9')