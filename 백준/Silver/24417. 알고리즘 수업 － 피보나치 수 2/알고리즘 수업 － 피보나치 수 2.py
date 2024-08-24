import sys
input = lambda: sys.stdin.readline().rstrip()


def matrix_mult(A, B, mod):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]


def matrix_pow(M, exp, mod):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = M

    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        exp //= 2

    return result


def fibonacci(N, mod):
    if N == 0:
        return 0
    if N == 1 or N == 2:
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, N - 1, mod)

    return result[0][0]


def main():
    N = int(input())
    std = 1000000007
    fib_value = fibonacci(N, std)
    print(fib_value, N - 2)


if __name__ == '__main__':
    main()