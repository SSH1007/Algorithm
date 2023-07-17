N = int(input())
for _ in range(N):
    A, B = input().split()
    if sorted(A) == sorted(B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')