# https://www.spoj.com/problems/SOCIALNE/fbclid=IwAR17NQ5giSLBhjyAwpxI16vNBLBKHLoDsCEkIfg5JQj2CrTGF9CmwilqAO4
INF = 1e9
from collections import defaultdict
def floy_war_shall(graph, dist):
    for i in range(len_matrix):
        for j in range(len_matrix):
            # update dist
            dist[i][j] = graph[i][j]
    for k in range(len_matrix):
        for i in range(len_matrix):
            for j in range(len_matrix):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == '__main__':
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        # get the matrix  from adjency matrix m*m
        # we can build , the shortest should be 2 => it's mean they can work
        first_line = input()
        len_matrix = len(first_line)
        # try to build graph, distance, path( trace matrix)
        graph = [[None for i in range(len_matrix)] for j in range(len_matrix)]
        dist = [[None for i in range(len_matrix)] for j in range(len_matrix)]
        path = [[None for i in range(len_matrix)] for j in range(len_matrix)]

        # update graph firstly:
        for j in range(len_matrix):
            if j == 0:
                value = 0
            elif first_line[j] == 'N':
                value = INF
            else:
                value = 1

            graph[0][j] = value
        for i in range(1, len_matrix):
            line = input()
            for j in range(len_matrix):
                if j == i:
                    value = 0
                elif line[j] == 'N':
                    value = INF
                else:
                    value = 1
                graph[i][j] = value
        dist = floy_war_shall(graph, dist)
        max = defaultdict(list)
        for index, row in enumerate(dist):
            count = 0
            for j in row:
                if j == 2:
                    count += 1
            max[count].append(index)
        max_key = sorted(max.keys())[-1]
        max_index = sorted(max[max_key])[0]
        print('{} {}'.format(max_index, max_key))
