# 피보나치 수를 행렬 제곱으로 푸는 문제
mod = 1000000007
n = int(input())


# 행렬 곱셈 정의
def powerMatrix(matrixA, matrixB):
    resultMatrix = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j]
            resultMatrix[i][j] %= mod
    return resultMatrix


# 단위행렬
identityMatrix = [[1, 0], [0, 1]]
# 피보나치 행렬
fibonacciMatrix = [[1, 1], [1, 0]]

# 13171번 문제의 분할 정복을 통한 거듭제곱 활용
while n:
    # n이 홀수라면
    if n & 1:
        identityMatrix = powerMatrix(identityMatrix, fibonacciMatrix)
    fibonacciMatrix = powerMatrix(fibonacciMatrix, fibonacciMatrix)
    n //= 2

print(identityMatrix[0][1])