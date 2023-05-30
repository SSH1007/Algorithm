import sys
input = sys.stdin.readline
while True:
    S = input().rstrip()

    if S == "CU":
        print("see you")
    elif S == ":-)":
        print("I’m happy")
    elif S == ":-(":
        print("I’m unhappy")
    elif S == ";-)":
        print("wink")
    elif S == ":-P":
        print("stick out my tongue")
    elif S == "(~.~)":
        print("sleepy")
    elif S == "TA":
        print("totally awesome")
    elif S == "CCC":
        print("Canadian Computing Competition")
    elif S == "CUZ":
        print("because")
    elif S == "TY":
        print("thank-you")
    elif S == "YW":
        print("you’re welcome")
    elif S == "TTYL":
        print("talk to you later")
        exit(0)
    else:
        print(S)