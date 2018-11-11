# http://codeforces.com/contest/557/problem/B
n, w = list(map(int, input().split()))
teapots = list(map(int, input().split()))

sorted_teapots = sorted(teapots)
min_teapot_women = sorted_teapots[0]
# get min of tea man
min_teapot_man = sorted_teapots[n]/2
# get full = min(3*n*min(min_women, min_man/), w)
# handle latter
max_w = min(3 * n * min(min_teapot_women, min_teapot_man), w)
print(max_w)