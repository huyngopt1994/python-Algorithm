numb_of_test = int(input())
for _ in range(numb_of_test):
    n, x = list(map(int, input().split()))
    arrays = set(map(int, input().split()))  # convert it into set( hastable)
    if len(arrays) == x:
        print('Good')
    elif len(arrays) > x:
        print('Average')
    else:
        print('Bad')
