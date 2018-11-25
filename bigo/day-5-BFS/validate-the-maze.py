# https://www.spoj.com/problems/MAKEMAZE/fbclid=IwAR1qCNiAcybrweV9haxuL-auJg99ShNY8jvp2Qg66CHzy0IYFXEW6WLjqng

import queue


class Pair():
    def __init__(self, a, b):
        self.x = a
        self.y = b


def is_valid(u, maze, row, col):
    # very is a point is valid or not
    return u.x >= 0 and u.x < row and u.y >= 0 and u.y < col and maze[u.x][u.y] == '.'


def BFS(start, end, maze, row, col):
    """

    :param start: node for start.
    :param end: node for end.
    :param maze: list of strings.
    :return:
    """
    dh = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # Build visited
    visited = [[False for xx in range(col)] for yy in range(row)]
    visited[start.x][start.y] = True

    # build a Queue
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        for k in range(4):
            v = Pair(u.x + dh[k], u.y + dc[k])
            if is_valid(v, maze, row, col) and not visited[v.x][v.y]:
                visited[v.x][v.y] = True
                if v.x == end.x and v.y == end.y:
                    # we find this node
                    return True
                q.put(v)
    return False


if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        # firstly need to check
        row, col = list(map(int, input().split()))
        maze = []
        # we just have 2 dots in border following this logic
        # loop per row : and append the input
        for _ in range(row):
            maze.append(input())
        points = []
        # loop for  per row
        for i in range(0, row):
            for j in range(0, col):
                if maze[i][j] == '.' and (i == 0 or j == 0 or i == row - 1 or j == col - 1):
                    points.append(Pair(i, j))

        if len(points) == 2:
            if BFS(points[0], points[1], maze, row, col):
                print('valid')
            else:
                print('invalid')
        else:
            print('invalid')
