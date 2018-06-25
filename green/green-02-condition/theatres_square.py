# Link problem : http://codeforces.com/problemset/problem/1/A
dai, rong, gach = map(int,input().split())

if dai % gach ==0:
    dai_gach = dai / gach
else:
    dai_gach = dai//gach +1

if rong % gach ==0:
    rong_gach = dai / gach
else:
    rong_gach = dai//gach +1


num_gach = (rong_gach*dai_gach)
print(num_gach)