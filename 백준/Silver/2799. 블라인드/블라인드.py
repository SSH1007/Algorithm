import sys
input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
info = [input() for _ in range(5*M+1)]
test = ''
for j in range(1, 5*N+1, 5):
    for i in range(5*M+1):
        test += info[i][j:j+4]

test = test.split('####')
target = {'................': 0, '****............': 0
        , '********........': 0, '************....': 0
        , '****************': 0}

for i in test:
    if i in target:
        target[i] += 1
for item in target:
    print(target[item], end=' ')