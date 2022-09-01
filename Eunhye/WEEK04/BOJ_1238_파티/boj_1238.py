import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, X = map(int,input().split())
adj = defaultdict(list)

for _ in range(M):
  v1, v2, w = map(int,input().split())
  heappush(adj[v1],(w, v2))

def dijkstra(src, adj):
  dist = [float("inf") for _ in range(N+1)]
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    w, v = heappop(hq)
    for nw, nv in adj[v]:
      nw += w
      if dist[nv] > nw:
        dist[nv] = nw
        heappush(hq, (nw, nv))
  return dist

dist = dijkstra(X, adj)
dist[0] = 0
for i in range(1, N+1):
  if i == X:
    dist[i] = 0
    continue
  to_x = dijkstra(i, adj)
  dist[i] += to_x[X]

print(max(dist))