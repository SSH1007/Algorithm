import sys
input = sys.stdin.readline
dic = {'E':'I','I':'E','S':'N','N':'S','T':'F','F':'T','J':'P','P':'J'}
mbti = input().rstrip()
dap = ''
for m in mbti:
    dap += dic[m]
print(dap)