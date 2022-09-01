# 파티
import heapq
import sys

INF = 10**9
N, M, X = map(int, sys.stdin.readline().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    A[a].append((c, b))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    d = [INF] * (N + 1)
    d[s] = 0
    while q:
        dist, curr = heapq.heappop(q)
        if d[curr] < dist:
            continue
        for next_dist, next in A[curr]:
            next_dist += dist
            if d[next] > next_dist:
                d[next] = next_dist
                heapq.heappush(q, (next_dist, next))
    return d

ans = 0
for i in range(1, N + 1):
    a = dijkstra(i)
    b = dijkstra(X)
    ans = max(ans, a[X] + b[i])

print(ans)