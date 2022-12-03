# 선수의 수 N
N = int(input())
# 가능한 성의 첫 글자들의 리스트
first = []
# 딕셔너리로 첫 글자가 같은 선수 수를 세자
dic = dict()
# 선수의 수만큼 반복문을 돌면서 성 첫글자마다 세주자
for _ in range(N):
    f = input()[0]
    if f in dic:
        dic[f]+=1
    else:
        dic[f]=1

# 딕셔너리의 아이템들을 순회하면서 
# 성의 첫글자가 같은 선수가 5명보다 많은 놈들만 추출
newdic = dic.items()
for nd in newdic:
    if nd[1]>=5:
        first.append(nd[0])
# 추출한 리스트가 비어있다면 PREDAJA 출력하고,
# 아니면 문자열로 합쳐서 출력(알파벳 순서대로)
if first:
    first.sort()
    print(('').join(first))
else:
    print('PREDAJA')