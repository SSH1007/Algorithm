import sys
input = sys.stdin.readline

first = [500,300,200,50,30,10]
second = [512,256,128,64,32] 
firstPrize, secondPrize = [0], [0]
for i in range(6):
    firstPrize += [first[i] for _ in range(i+1)]
for i in range(5):
    secondPrize += [second[i] for _ in range(2**i)] 
    
T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    if a>=len(firstPrize):
        a = 0
    if b>=len(secondPrize):
        b = 0
    print((firstPrize[a]+secondPrize[b])*10000)