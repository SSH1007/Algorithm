import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N, K = map(int, input().split())
    S = input()
    
    if '0'*K in S:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()