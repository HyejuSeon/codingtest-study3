import sys
sys.setrecursionlimit(10**7)

n = int(input())
tree = [[] for _ in range(n+1)]
result, max_node = 0, 0
for _ in range(n-1):
  p, ch, w = map(int, input().split())
  tree[p].append((ch, w))
  tree[ch].append((p, w))
  

def dfs(src, dist, visited):
  global result, max_node
  visited[src] = 1
  if dist > result:
    result = dist
    max_node = src
  for ch, w in tree[src]:
    if not visited[ch]:
      dfs(ch, dist+w, visited)

visited = [0 for _ in range(n+1)]

dfs(1, 0, visited[:])
dfs(max_node, 0, visited[:])

print(result)