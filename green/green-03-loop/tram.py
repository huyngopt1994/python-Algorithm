"http://codeforces.com/problemset/problem/116/A"
"""
input : 
4
0 3
2 5
4 2
4 0
"""

num_of_trams = int(input())
max = 0
current_tram = 0
for _ in range(num_of_trams):
    out_pass, in_pass  = map(int,input().split())
    current_tram = current_tram + in_pass - out_pass
    if current_tram > max:
        max = current_tram

print(max)