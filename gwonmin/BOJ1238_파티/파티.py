import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_idx,node_cost in graph[now]:
            cost = node_cost + dist

            if cost < distance[node_idx]:
                distance[node_idx] = cost
                heapq.heappush(q,(cost, node_idx))

    return distance

result = 0
for i in range(1,n+1):
    temp = dijkstra(i)[x] + dijkstra(x)[i]
    if result < temp:
        result = temp

print(result)

'''
input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)
'''