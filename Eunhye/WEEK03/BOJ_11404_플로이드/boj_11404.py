import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[math.inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  if c < graph[a-1][b-1]: graph[a-1][b-1] = c

for k in range(n):
  for i in range(n):
    for j in range(n):
      if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

for a in range(n):
  for b in range(n):
    if graph[a][b] == math.inf or a == b:
      graph[a][b] = 0
for g in graph:
  print(*g, sep=" ")