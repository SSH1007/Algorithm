N = int(input())
# 암호화된 16진수 정수(str)를 10진수(int)로 변경
hex_message = list(input().split())
dec_message = [int(h, 16) for h in hex_message]

# 문자가 아닌 경우들(' ', '.')을 '0'~'9' 키로 XOR 연산한 값을 저장
notChar = set()
for i in ' .':
    for j in '0123456789':
        notChar.add(int(hex(ord(i)), 16) ^ int(hex(ord(j)),16))

dap = ''
for d in dec_message:
    if not d in notChar:
        dap += '-'
    else:
        dap += '.'
print(dap)