# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=499&fbclid=IwAR0-g2uszCYZxaymc19szVkgyTa606LYKsyxxJkq3PU8WpywHQh5cCTuDyc
"""
The problem just sure the sum of a cycle is negative => if it will make wrong
"""
INF = int(1e9)


def check_have_negative_weight_cycle(graph, dist, path, s, n, m):
    dist[s] = 0

    for i in range(1, n):
        for j in range(m):
            u = graph[j][0]
            v = graph[j][1]
            w = graph[j][2]

            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    # check if it have a negative cycle(negative cycle meaning sum of weights in a cycle is negative)
    for i in range(m):
        u = graph[i][0]
        v = graph[i][1]
        w = graph[i][2]

        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        num_of_uni, num_of_wh = list(map(int, input().split()))
        graph = []
        # build array faster than building by hash table.
        dist = [INF for i in range(num_of_uni)]
        path = [-1 for i in range(num_of_uni)]

        for _ in range(num_of_wh):
            start_uni, end_uni, time = list(map(int, input().split()))
            graph.append([start_uni, end_uni, time])
        s = 0
        result = check_have_negative_weight_cycle(graph=graph, dist=dist, path=path, s=0, n=num_of_uni, m=num_of_wh)
        if not result:
            print('possible')
        else:
            print('not possible')
