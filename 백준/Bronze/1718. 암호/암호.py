# 평문 입력
word = input()
# 암호화 키 입력
key = input()
# 암호화 결과 초기화
dap = ''
for w in range(len(word)):
    # 만약 공백이면 공백 문자 그대로 더하고 컨티뉴
    if ord(word[w]) == 32:
        dap += ' '
        continue
    # 해당 암호화 순번의 알파벳
    kk = key[w%len(key)]
    # 암호화한 문자를 더한다
    dap += chr((ord(word[w])-ord(kk)-1)%26+97)
print(dap)