import queue

MAX = 100
INF = int(1e9)


# build node (include dist and id)
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        # Using compare with dist
        return self.dist <= other.dist


def Dijkstra(s):
    # Firstly create a queue and put the node with id=s , and dist=0
    pq = queue.PriorityQueue()
    pq.put(Node(id=s, dist=0))
    # set dist table at s = 0
    dist[s] = 0

    # work when this queue is empty
    while pq.empty() == False:
        # get the min distance
        top = pq.get()
        # get id and dist
        u = top.id
        w = top.dist

        # verify neighbor of this min:
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                # update dist
                dist[neighbor.id] = w + neighbor.dist
                # add into queue
                pq.put(Node(neighbor.id, dist[neighbor.id]))

                # update path
                path[neighbor.id] = u


if __name__ == '__main__':
    n = int(input())
    source, destination = 0, 4

    graph = [[] for i in range(n + 5)]
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append(Node(j, d[j]))
    Dijkstra(source)
    ans = dist[destination]
    print(ans)
