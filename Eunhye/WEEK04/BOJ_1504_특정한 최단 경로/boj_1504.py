import sys

input = sys.stdin.readline

import math
from collections import defaultdict
from heapq import heappush, heappop

N, E = map(int, input().split())

adj = defaultdict(list)

for _ in range(E):
  a, b, c = map(int, input().split())
  heappush(adj[a], (c, b))
  heappush(adj[b], (c, a))

def dijkstra(src):
  dist = [ math.inf for _ in range(N+1)]
  dist[src] = 0
  hq = [(0, src)]

  while hq:
    w, v = heappop(hq)
    if w > dist[v]:
      continue
    for nw, nv in adj[v]:
      nw += w
      if dist[nv] > nw:
        dist[nv] = nw
        heappush(hq, (nw, nv))
  return dist

v1, v2 = map(int, input().split())
dist1 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)
way1 = dist1[v1] + distv1[v2] + distv2[N]
way2 = dist1[v2] + distv2[v1] + distv1[N]

answer = min(way1, way2)
print(-1 if answer == math.inf else answer)