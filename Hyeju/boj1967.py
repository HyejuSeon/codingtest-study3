# 트리의 지름
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
A = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    A[a].append((b, c))
    A[b].append((a, c))

def dfs(n, d):
    global res, max_idx
    visited[n] = 1
    if res < d:
        res = d
        max_idx = n
    for next, next_dist in A[n]:
        if not visited[next]:
            dfs(next, next_dist + d)

res = 0
max_idx = 0
visited = [0] * (N + 1)
dfs(1, 0)
visited = [0] * (N + 1)
dfs(max_idx, 0)
print(res)
