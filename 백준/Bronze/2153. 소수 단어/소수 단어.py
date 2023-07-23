aaa = input()
dic = '*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = 0
for a in aaa:
    num += dic.index(a)

flag = False
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        flag = True
        break
if flag:
    print('It is not a prime word.')
else:
    print('It is a prime word.')