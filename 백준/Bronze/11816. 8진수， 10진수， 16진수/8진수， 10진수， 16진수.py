X = input()
if X.find('0x')==0:
    print(int(X,16))
elif X.find('0')==0:
    print(int(X,8))
else:
    print(X)