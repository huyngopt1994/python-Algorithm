# https://www.spoj.com/problems/MST/fbclid=IwAR0o8a5fepOkMWd9uwcd5sAbQi0lqeAL1IK30VBaQIEZLzqWQN7D26XwHxI
import queue

INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def print_mst():
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue
        ans += dist[i]
    print(ans)


def prim(src):
    pq = queue.PriorityQueue()  # Create a heap
    # put this node
    pq.put(Node(src, 0))  # add first node firstly
    dist[src] = 0

    while pq.empty() == False:
        # check if pq is not empty
        top = pq.get()
        # check this point
        u, d = top.id, top.dist
        visited[u] = True
        # start to verify it's neighbor
        for neighbor in graph[u]:
            v, w = neighbor.id, neighbor.dist
            if not visited[v] and w < dist[v]:
                # if this node is not visited and it is updated
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    # build graph ,dist and path firstly
    graph = [[] for _ in range(n)]
    dist = [INF for _ in range(n)]
    path = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    for _ in range(m):
        i, j, k = list(map(int, input().split()))
        # update graph
        graph[i - 1].append(Node(j - 1, k))
        graph[j - 1].append(Node(i - 1, k))
    prim(0)
    print_mst()
