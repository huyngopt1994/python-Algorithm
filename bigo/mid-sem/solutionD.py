from queue import Queue


def is_valid(u, row, col, bomb_nodes):
    # very is a point is valid or not

    return u[0] >= 0 and u[0] < row and u[1] >= 0 and u[1] < col and not bomb_nodes.get('{}_{}'.format(u[0], u[1]))


def bfs(start, end, bomb_nodes, row, col):
    """

    :param s: start node
    :param e: end node
    :param map: the map contain full node (r *c nodes)
    :param bomb_nodes: node contain bomb
    :param r: the length of row
    :param c: the length of column
    :return: the shortest distance from start node to end node
    """
    dh = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    q = Queue()
    visited = [[False for xx in range(col)] for yy in range(row)]
    dist = [[0 for xx in range(col)] for yy in range(row)]
    visited[start[0]][start[1]] = True
    q.put(start)
    while not q.empty():
        u = q.get()
        for k in range(4):
            v = [u[0] + dh[k], u[1] + dc[k]]

            if is_valid(v, row=row, col=col, bomb_nodes=bomb_nodes) and not visited[v[0]][v[1]]:
                visited[v[0]][v[1]] = True
                dist[v[0]][v[1]] = dist[u[0]][u[1]] + 1
                if v == end:
                    return dist[v[0]][v[1]]
                q.put(v)


r, c = list(map(int, input().split()))
while r != 0 and c != 0:
    rows = int(input())
    bomb_nodes = {}
    for _ in range(rows):
        custom_row = list(map(int, input().split()))
        for col in range(2, len(custom_row)):
            bomb_nodes['{}_{}'.format(custom_row[0], custom_row[col])] = 1
    r1, c1 = list(map(int, input().split()))
    s = [r1, c1]
    r1, c1 = list(map(int, input().split()))
    e = [r1, c1]

    print(bfs(start=s, end=e, bomb_nodes=bomb_nodes, row=r, col=c))
    r, c = list(map(int, input().split()))
