N = int(input())
dna = list(input())
# 염기서열표는 대각선을 기준으로 대칭임. 따라서 케이스는 6개만 준비
dic = {'AG':'C', 'AC':'A', 'AT':'G', 'GC':'T', 'GT':'A', 'CT':'G'}
# 비교용 변수 a와 b를 준비. b는 받은 염기서열의 맨 끝 글자를 pop
a, b = '', dna.pop()
# 받은 문자열의 길이가 0이 될때까지 반복
while len(dna)>0:
    # a에 현재 염기서열의 맨 끝 글자를 pop
    a = dna.pop()
    # 만약 a와 b가 같다면 그대로 패스
    if a==b:
        continue
    # AG, AC, AT, GC, GT, CT라면
    if a+b in dic.keys():
        # 그에 해당하는 염기로 b를 최신화
        b = dic[a+b]
    # GA, CA, TA, CG, TG, TC라면
    else:
        # 그에 해당하는 염기로 b를 최신화
        b = dic[b+a]
# b 출력
print(b)