import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)


parents = [0 for _ in range(N+1)]
def dfs(parent):
  if not tree[parent]:
    return
  for num in tree[parent]:
    if not parents[num]:
      parents[num] = parent
      dfs(num)
  
dfs(1)
for i in range(2, N+1):
  print(parents[i])