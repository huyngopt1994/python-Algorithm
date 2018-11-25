number = int(input())
my_string = input().strip().lower()
from string import ascii_lowercase

is_good = True

for c in ascii_lowercase:
    if c not in my_string:
        is_good =False
        break

if is_good:
    print('YES')
else:
    print('NO')
