def Rev(n):
    dap = ''    # 빈 문자열 생성
    for i in range(len(str(n))):    # 인자로 받은 숫자의 자리수만큼 반복
        dap+=str(n)[i]              # 빈 문자열에 순서대로 더한다.
    return int(dap[::-1])           # 문자열이 된 수를 역순으로 뒤집고, 그 값을 정수로 바꿔 반환한다.

X, Y = map(int,input().split()) # 두 수 X,Y를 정수로 받는다
print(Rev(Rev(X)+Rev(Y)))       # Rev(Rev(X)+Rev(Y))를 출력