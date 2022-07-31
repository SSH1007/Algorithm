ABC = list(map(int,input().split()))
st = input()
ABC = sorted(ABC)
for s in st:
    print(ABC[ord(s)-65],end=' ')