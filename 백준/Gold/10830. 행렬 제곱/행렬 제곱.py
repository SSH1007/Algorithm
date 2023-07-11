# 제수와 변수, 행렬 입력 및 설정
mod = 1000
N, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


# 행렬 곱셈 정의
def powerMatrix(n, matrixA, matrixB):
    resultMatrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j]
            # 숫자가 너무 커질 수 있으니 mod로 나눈 값으로 저장
            resultMatrix[i][j] %= mod
    return resultMatrix


# 분할 정복 함수
def devidePower(N, B, matrix):
    # 제곱 안하면 각 행렬값을 mod의 나머지값으로 바꿔주고 반환
    if B == 1:
        for m in matrix:
            for n in range(N):
                m[n] %= mod
        return matrix
    # 한번만 제곱하면 위의 함수 돌려서 반환
    elif B == 2:
        return powerMatrix(N, matrix, matrix)
    else:
        # 분할된 행렬
        tmp = devidePower(N, B//2, matrix)
        # 제곱횟수가 홀수면 (AAAAA = ((A**2)**2)*A)
        # 따라서 분할 제곱 값에 한번더 행렬을 곱해준다
        if B & 1:
            return powerMatrix(N, powerMatrix(N, tmp, tmp), matrix)
        # 제곱횟수가 짝수면 (AAAA = ((A**2)**2))
        else:
            return powerMatrix(N, tmp, tmp)


for d in devidePower(N, B, matrix):
    print(*d)