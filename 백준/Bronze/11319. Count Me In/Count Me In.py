V = ['A','E','I','O','U','a','e','i','o','u']
S = int(input())
for _ in range(S):
    sentence = ''.join(input().split())
    l = len(sentence)
    v = 0
    for s in sentence:
        if s in V:
            v += 1
    print(l-v, v)