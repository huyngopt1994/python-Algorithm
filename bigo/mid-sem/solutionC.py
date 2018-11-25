k, n, w = list(map(int, input().split()))

total_have_to_buy = 0

for i in range(1, w + 1):
    total_have_to_buy += i * k

dollar_he_borrow = total_have_to_buy - n

if dollar_he_borrow < 0:
    dollar_he_borrow = 0

print(dollar_he_borrow)
