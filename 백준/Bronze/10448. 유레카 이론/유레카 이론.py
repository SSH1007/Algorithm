tri = []
n, m = 1, 1
while n < 1000:
    tri.append(n)
    m += 1
    n += m

def test(K):
    for i in tri:
        for j in tri:
            for k in tri:
                if i+j+k == K:
                    return 1
    return 0

T = int(input())
for _ in range(T):
    dap = test(int(input()))
    print(dap)