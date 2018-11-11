# http://codeforces.com/problemset/problem/439/B
n, x = list(map(int, input().split()))
chapters_of_subject = list(map(int, input().split()))

# sorted this subject
sorted_chapters_of_subject = sorted(chapters_of_subject)
total = 0
for chapters in sorted_chapters_of_subject:
    total += (chapters * x)
    x -= 1
    if x < 1:
        x = 1

# time complexity = o(n)
print(total)
