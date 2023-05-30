import sys
input = sys.stdin.readline
A, B, C = map(int, input().rstrip().split())
dap = A/1000000*(229*324)*2 + B/1000000*(297*420)*2 + C/1000000*(210*297)
print(dap)