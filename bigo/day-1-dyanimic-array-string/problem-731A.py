# http://codeforces.com/problemset/problem/731/A
import string

list_apha = list(string.ascii_lowercase)
custom_alphas = list(input())
current_index = 0
result = 0
for alpha in custom_alphas:
    new_index = list_apha.index(alpha.lower())
    distance_1 = abs(new_index - current_index)
    distance_2 = 26 - distance_1
    steps = min(distance_1, distance_2)
    result += steps
    current_index = new_index

print(result)
