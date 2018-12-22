numb_of_testcases = int(input())
for _ in range(numb_of_testcases):
    n, m = list(map(int, input().split()))
    full_candidates = list(map(int, input().split()))
    built_existed = {}
    for i in full_candidates[:n]:
        built_existed[i] = True

    for i in full_candidates[n:]:
        if built_existed.get(i):
            print('YES')
        else:
            print('NO')
            built_existed[i]= True
