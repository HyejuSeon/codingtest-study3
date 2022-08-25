import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


for i in range(1,N):
  graph[0][i] += graph[0][i-1]
  graph[i][0] += graph[i-1][0]

for x in range(1, N):
  for y in range(1,N):
    graph[x][y] += graph[x-1][y] + graph[x][y-1] - graph[x-1][y-1]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  exclude = 0
  if x1 > 1:
    exclude += graph[x1-2][y2-1]
  if y1 > 1:
    exclude +=  graph[x2-1][y1-2]
  if x1 > 1 and y1 > 1:
    exclude -=  graph[x1-2][y1-2]
  print(graph[x2-1][y2-1]-exclude)