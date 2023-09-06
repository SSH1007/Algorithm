N = int(input())
S = input()
big = S.count('bigdata')
sec = S.count('security')
if big > sec:
    print('bigdata?')
elif big < sec:
    print('security!')
else:
    print('bigdata? security!')