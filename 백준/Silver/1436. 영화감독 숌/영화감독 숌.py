N = int(input())
doom_num = 666
cnt = 0
while 1:
    if '666' in str(doom_num):
        cnt+=1
    if cnt == N:
        break
    doom_num+=1
print(doom_num)