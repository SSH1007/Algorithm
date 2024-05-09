import sys
input = sys.stdin.readline
S, P = map(int, input().rstrip().split())
DNA = input().rstrip()
ACGT = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
A, C, G, T = map(int, input().rstrip().split())
for p in range(P):
    ACGT[DNA[p]] += 1
s, e = 0, P
cnt = 0
while e <= S:
    if ACGT['A'] >= A and ACGT['C'] >= C and ACGT['G'] >= G and ACGT['T'] >= T:
        cnt += 1
    ACGT[DNA[s]] -= 1
    s += 1
    if e >= S:
        break
    ACGT[DNA[e]] += 1
    e += 1
print(cnt)