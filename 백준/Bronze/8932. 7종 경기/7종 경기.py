T = int(input())
for _ in range(T):
    a, b, c, d, e, f, g = map(int, input().split())
    dap = 0
    dap += int(9.23076*((26.7-a)**1.835))
    dap += int(1.84523*((b-75)**1.348))
    dap += int(56.0211*((c-1.5)**1.05))
    dap += int(4.99087*((42.5-d)**1.81))
    dap += int(0.188807*((e-210)**1.41))
    dap += int(15.9803*((f-3.8)**1.04))
    dap += int(0.11193*((254-g)**1.88))
    print(dap)