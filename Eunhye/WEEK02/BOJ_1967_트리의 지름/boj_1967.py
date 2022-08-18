V = int(input())
tree = [[] for _ in range(V+1)]
result, max_node = 0, 0
for _ in range(V):
  input_lst = list(map(int, input().split()))
  for i in range(1, len(input_lst)-1, 2):
    tree[input_lst[0]].append(tuple(input_lst[i:i+2]))

def dfs(src, dist, visited):
  global result, max_node
  visited[src] = 1
  if dist > result:
    result = dist
    max_node = src
  for v, d in tree[src]:
    if not visited[v]:
      dfs(v, dist+d, visited)

visited = [0 for _ in range(V+1)]

dfs(1, 0, visited[:])
dfs(max_node, 0, visited[:])

print(result)