# http://algote.com/team/problem_v1.php?id=214
INF = 1e9


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def find_the_shortest_distance_with_bellman_ford(dist, graph):
    s = 0  # hard core with only this home work
    dist[s] = 0
    for _ in range(num_conjuncts - 1):  # loop num_conjunts
        for j in range(num_roads):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


if __name__ == '__main__':
    number_of_testcases = int(input())
    for i in range(number_of_testcases):
        input()  # skip one line
        num_conjuncts = int(input())
        conjuncts = list(map(int, input().split()))
        num_roads = int(input())
        roads = []
        for _ in range(num_roads):
            src, des = list(map(int, input().split()))
            weight = (conjuncts[des - 1] - conjuncts[src - 1]) ** 3  # minus 1 because index start from 0
            roads.append(Edge(source=src - 1, target=des - 1, weight=weight))

        dist = [INF for _ in range(num_conjuncts)]
        dist = find_the_shortest_distance_with_bellman_ford(dist=dist, graph=roads)
        q = int(input())
        des = []
        ans = []
        for _ in range(q):
            des = int(input())
            if dist[des - 1] < 3 or dist[des - 1] == INF:
                ans.append('?')
            else:
                ans.append(str(dist[des - 1]))

        print('Case {}:'.format(i + 1))
        for a in ans:
            print(a)
