n = int(input())

def print_stair(space, star):
    if space == 0:
        return 0
    else:
        print(' '*(space-1),'#'*(star+1),sep='')
        return print_stair(space-1,star+1)
print_stair(n,0)

