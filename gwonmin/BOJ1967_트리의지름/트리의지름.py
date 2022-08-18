from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    info = list(map(int,input().split()))
    graph[info[0]].append([info[1], info[2]])
    graph[info[1]].append([info[0], info[2]])

def bfs(start):
    max_node = 0
    max_dist = 0
    visit = deque()
    visit.append(start)
    visited = [start[0]]

    while visit:
        par_node, par_dist = visit.popleft()

        if par_dist > max_dist:
            max_dist = par_dist
            max_node = par_node

        for child_node, child_dist in graph[par_node]:
            if child_node not in visited:
                visit.append([child_node,par_dist+child_dist])
                visited.append(child_node)

    return max_node, max_dist

temp_node,_ = bfs([1,0])
_,result = bfs([temp_node,0])
print(result)