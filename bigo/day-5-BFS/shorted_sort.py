# https://www.hackerrank.com/challenges/bfsshortreach/problem?h_r=internal-search

from queue import Queue


def get_distance(start, end, final_path):
    new_key = end
    result = []
    while new_key != -1:
        result.append(new_key)
        new_key = final_path[new_key]
        if new_key == start:
            result.append(new_key)
            break
    if not result or (result and result[-1] != start):
        return -1
    else:
        return (len(result) - 1) * 6


# Complete the bfs function below.
def bfs(n, m, edges, s):
    """

    :param n: number of node
    :param m: number of edges
    :param edges: array of edges
    :param s: node start
    :return:
    """
    visited = {}
    path = {}
    graph = {}
    # init visted
    for node in range(1, n + 1):
        visited[node] = False
        path[node] = -1
        graph[node] = set()

    # add graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    for key in graph:
        graph[key] = list(graph[key])

    m_q = Queue()
    # we should put the first is s
    m_q.put(s)
    while (not m_q.empty()):
        node = m_q.get()

        checked_nodes = graph[node]
        for checked_node in checked_nodes:
            if not visited[checked_node]:
                # this the first time, update path
                path[checked_node] = node
                m_q.put(checked_node) # instead of storing path , we can store distance
                visited[checked_node] = True
    # get the distance from start to the end
    result = []
    for end in graph.keys():
        if end != s:
            result.append(get_distance(s, end, path))
    return result


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        print(' '.join(map(str, result)))
