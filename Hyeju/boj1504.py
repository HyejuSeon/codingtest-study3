# 특정한 최단 경로
import sys
from heapq import heappop, heappush
INF = 10**9
N, E = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    A[a].append((c, b))
    A[b].append((c, a))
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(s):
    d = [INF] * (N + 1)
    q = []
    heappush(q, (0, s))
    d[s] = 0
    while q:
        dist, curr = heappop(q)
        for next_dist, next in A[curr]:
            next_dist += dist
            if d[next] > next_dist:
                d[next] = next_dist
                heappush(q, (next_dist, next))
    return d

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)
ans = min(d1[v1] + d2[v2] + d3[N], d1[v2] + d3[v1] + d2[N])
print(ans if ans < INF else -1)