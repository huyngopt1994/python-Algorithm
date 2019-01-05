# https://www.hackerrank.com/challenges/bon-appetit/problem?h_r=next-challenge&h_v=zen
def calculate_actual_money(index, orders):
    sum = 0
    for i, value in enumerate(orders):
        if i == index:
            continue
        sum += value
    return sum // 2


total, index = map(int, input().split())
orders = list(map(int, input().split()))
charged = int(input())

result = calculate_actual_money(index, orders)

final_result = charged - result
if final_result:
    print(final_result)
else:
    print('Bon Appetit')
