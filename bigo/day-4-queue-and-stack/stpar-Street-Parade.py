# https://www.spoj.com/problems/STPAR/fbclid=IwAR3DNOqkth79CD9rurn55e5Gf8Ph_3oV6ZztxDi9qG4pBYfsAljL4TnWSCE
while int(input()) != 0:
    main_queue = list(map(int, input().split()))
    # first in first out
    count = 1
    side_road = []  # stack # first in last out
    while len(main_queue) > 0:
        if main_queue[0] == count:
            main_queue.pop(0)  # pop in first element
            count += 1
        elif side_road and side_road[-1] == count:
            side_road.pop()  # pop the last element
            count += 1
        else:
            side_road.append(main_queue.pop(0))
    # check side road is broken (it should be descending)
    if len(side_road) == 0 or (side_road == sorted(side_road, reverse=True)):
        print('yes')
    else:
        print('no')
