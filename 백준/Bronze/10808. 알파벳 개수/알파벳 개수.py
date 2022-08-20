atoz = [0]*26
txt = input()
for t in txt:
    atoz[ord(t)-97]+=1
print(*atoz)