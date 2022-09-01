import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (n+1)
    q = []

    heapq.heappush(q,(start,0))
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for node_idx, node_cost in graph[now]:
            cost = node_cost + dist
            if cost < distance[node_idx]:
                distance[node_idx] = cost
                heapq.heappush(q,(node_idx, cost))
    return distance

a = dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[n]
b = dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[n]
if min(a,b) >= INF:
    print(-1)
else:
    print(min(a,b))

