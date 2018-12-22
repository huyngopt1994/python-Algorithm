# http://codeforces.com/problemset/problem/424/B
ALLOW = 1000000
point, num_of_cititzens = list(map(int, input().split()))

result = 0


def cal_sum_power(number_1, number_2):
    return sum(number_1 ** 2 + number_2 ** 2)


for _ in range(point):
    if num_of_cititzens >= ALLOW:
        break
    x, y, number = list(map(int, input().split()))
    # build BST in here


# After complete this building try to transver
