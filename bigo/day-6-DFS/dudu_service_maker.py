# https://www.urionlinejudge.com.br/judge/en/problems/view/1610
"""
We will seperate into three states 1. Checked but still in path
2. Checked but done in a path
0. don't check yet.

psuedo code
handle DFS function: O(V+E)
DFS(u):
visited[u] = 1
for v in graph[u] (check adjent v of u):
    if visted[v] == 0:
        if DFS(v)== True
            return True
    elif visisted[v] == 1: O(1)
        return True
    visited[u] =2
return False

Logic homework
res= False
for i 1 -> N
    if visited[i] == 0:
        if DFS(i) == True
            res= True
            break

if res == true
=> SIM
else:
=> NAO
"""