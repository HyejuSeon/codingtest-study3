# 트리의 지름
from sys import stdin
from collections import deque

N = int(stdin.readline())
A = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, stdin.readline().split())
    A[a].append((b, c))
    A[b].append((a, c))

def bfs(s):
    q = deque()
    q.append(s)
    dist[s] = 0
    while q:
        curr = q.popleft()
        for e, w in A[curr]:
            if dist[e] == -1:
                dist[e] = dist[curr] + w
                q.append(e)

dist = [-1] * (N + 1)
bfs(1)
max_dist = max(dist)
max_idx = dist.index(max_dist)
dist = [-1] * (N + 1)
bfs(max_idx)
print(max(dist))
