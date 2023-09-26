number = set([i for i in range(2, 1000001)])
for n in range(2, 1000001):
    prime = set([i for i in range(2*n, 1000001, n)])
    number.difference_update(prime)

import sys
input = sys.stdin.readline

while 1:
    N = int(input().rstrip())
    if N == 0:
        break
    for num in number:
        if N-num in number:
            print('%d = %d + %d' % (N, num, N-num))
            break
    else:
        print("Goldbach's conjecture is wrong.")