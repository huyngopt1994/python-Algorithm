parent = []
ranks = []


def make_set(n):
    """
    Build a make set for initial state build parent is itself. O(n)
    :return:
    """
    global parent
    parent = [i for i in range(n)]


def find_set(u):
    """find the representative of a set. Bad case is O(n)"""
    if u == parent[u]:
        return u
    return find_set(parent[u])


def union_set(u, v):
    """Try to add an element into a set or combine 2 sets together.If 2 elements wered associated we bypass. O(n)"""
    up = find_set(u)
    vp = find_set(v)
    parent[up] = vp


n, m = list(map(int, input().split()))
# we can get student and m of pairs
make_set(n)
for _ in range(m):
    # try to loop per pair
    u, v = list(map(int, input().split()))
    union_set(u, v)

print(parent)
