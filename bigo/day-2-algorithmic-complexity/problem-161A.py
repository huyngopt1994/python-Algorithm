# http://codeforces.com/problemset/problem/161/A

n, m, x, y = list(map(int, input().split()))
a_s = list(map(int, input().split()))
b_s = list(map(int, input().split()))

count = 0
my_result = []
j = 0
for i in range(n):
    while j <= m-1:
        if a_s[i] - x <= b_s[j] <= a_s[i] + y:
            # we find mapping between i and j => increase i and j
            count += 1
            my_result.append([i + 1, j + 1])
            j += 1
            break
        elif b_s[j] < a_s[i] - x:
            j += 1
            # j is lower than i => should increase j
            continue
        else:
            # increase i
            break
print(count)
for item in my_result:
    print('{} {}'.format(item[0], item[1]))
