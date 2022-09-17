import sys
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    operation = sys.stdin.readline().strip().split()
    if len(operation) == 1:
        if operation[0] == "all":
            S = set([i for i in range(1,21)])
        elif operation[0] == "empty":
            S = set()
        continue
    command, number = operation[0], operation[1]
    number = int(number)
    if command == "add":
        S.add(number)
    elif command == "remove":
        S.discard(number)
    elif command == "check":
        if number in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if number in S:
            S.discard(number)
        else:
            S.add(number)