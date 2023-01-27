# 소문자 26개분의 0 리스트 생성
alphabet = [0]*26
A = input()
B = input()
# 첫번째 단어의 각 알파벳이 몇개나 있는지 덧셈으로 계산
for i in range(len(A)):
    alphabet[ord(A[i])-97]+=1
# 두번째 단어의 각 알파벳이 몇개나 있는지 뺄셈으로 계산
for i in range(len(B)):
    alphabet[ord(B[i])-97]-=1
# 합산 결과 알파벳이 0개라면 애너그램 관계에 속하는 알파벳이므로,
# 0개가 아닌 놈들을 전부 더하면 됨(절대값)
print(sum(map(abs,alphabet)))