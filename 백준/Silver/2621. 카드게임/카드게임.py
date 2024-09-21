import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    cards = [list(input().split()) for _ in range(5)]
    cards_color = {'R':0, 'B':0, 'Y':0, 'G':0}
    cards_cnt = [0]*10
    dap = 0
    for i in range(5):
        color, number = cards[i][0], cards[i][1]
        cards_color[color] += 1
        cards_cnt[int(number)] += 1
    n_cards = sorted([int(c[1]) for c in cards])
    if 5 in cards_color.values() and n_cards[0] == n_cards[1]-1 and \
        n_cards[1] == n_cards[2]-1 and n_cards[2] == n_cards[3]-1 and \
        n_cards[3] == n_cards[4]-1:
        dap = 900 + max(n_cards)
    elif max(cards_cnt) == 4:
        dap = 800 + cards_cnt.index(max(cards_cnt))
    elif 3 in cards_cnt and 2 in cards_cnt:
        dap = 700 + cards_cnt.index(3)*10 + cards_cnt.index(2)
    elif 5 in cards_color.values():
        dap = 600 + max(n_cards)
    elif n_cards[0] == n_cards[1]-1 and \
        n_cards[1] == n_cards[2]-1 and n_cards[2] == n_cards[3]-1 and \
        n_cards[3] == n_cards[4]-1:
        dap = 500 + max(n_cards)
    elif 3 in cards_cnt:
        dap = 400 + cards_cnt.index(3)
    elif cards_cnt.count(2) == 2:
        flag = False
        for i in range(10):
            if cards_cnt[i] == 2:
                if flag:
                    dap += i*10
                else:
                    dap += i
                    flag = True
        dap += 300
    elif 2 in cards_cnt:
        dap = 200 + cards_cnt.index(2)
    else:
        dap = 100 + max(n_cards)
    print(dap)


if __name__ == '__main__':
    main()