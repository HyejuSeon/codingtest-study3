# 트리의 지름
import sys
from collections import deque

V = int(sys.stdin.readline())
arr = [[] for _ in range(V + 1)]
dist = [-1 for _ in range(V + 1)]
def bfs(s):
    q = deque()
    q.append(s)
    dist[s] = 0
    while q:
        curr = q.popleft()
        for e, w in arr[curr]:
            if dist[e] == -1:
                dist[e] = dist[curr] + w
                q.append(e)

for _ in range(V):
    l = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(l) - 1, 2):
        arr[l[0]].append((l[i], l[i + 1]))

bfs(1)
max_dist = max(dist[1:])
max_idx = dist.index(max_dist)

dist = [-1 for _ in range(V + 1)]
bfs(max_idx)
print(max(dist[1:]))
