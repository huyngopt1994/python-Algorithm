MAX = 20
parent = []
ranks = []


def make_set():
    """
    Build a make set for initial state build parent is itself. O(n)
    :return:
    """
    global parent
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for _ in range(MAX + 5)]


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


if __name__ == '__main__':
    q = int(input())
    make_set()
    for i in range(q):
        u, v, q = map(int, input().split())
        if q == 1:
            union_set(u, v)
        elif q == 2:
            parent_u = find_set(u)
            parent_v = find_set(v)
            if parent_u == parent_v:
                print('1')
            else:
                print('0')
