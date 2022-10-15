import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)

# 산술평균
print(round(sum(lst)/N))

# 중앙값
lst.sort()
print(lst[N//2])

# 최빈값
dic = dict()
for l in range(len(lst)):
    if lst[l] not in dic.keys():
        dic[lst[l]]=1
    else:
        dic[lst[l]]+=1
sorted_dic = sorted(dic.items(), key=lambda x : x[1], reverse=True)
if len(sorted_dic)>1:
    if sorted_dic[0][1] == sorted_dic[1][1]:
        print(sorted_dic[1][0])
    else:
        print(sorted_dic[0][0])
else:
    print(sorted_dic[0][0])

# 범위
print(lst[-1]-lst[0])