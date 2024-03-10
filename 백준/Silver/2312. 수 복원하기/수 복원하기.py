def restore(N):
    i = 2
    dic = dict()
    while N > 1:
        if N%i == 0:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            N /= i
        else:
            i += 1
    return dic


N = int(input())
for _ in range(N):
    dap = list(restore(int(input())).items())
    for k, v in dap:
        print(k, v)