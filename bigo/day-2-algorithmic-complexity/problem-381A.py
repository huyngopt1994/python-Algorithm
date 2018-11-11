# http://codeforces.com/problemset/problem/381/A
number_of_card = int(input())
cards = list(map(int, input().split()))

score_s = 0
score_d = 0
is_s = True
for i in range(number_of_card):
    larger_card = 0
    if cards[0] >= cards[-1]:
        larger_card = cards[0]
        del cards[0]
    else:
        larger_card = cards[-1]
        del cards[-1]
    if is_s:
        score_s += larger_card
    else:
        score_d += larger_card
    is_s = not is_s

print('{} {}'.format(score_s, score_d))
