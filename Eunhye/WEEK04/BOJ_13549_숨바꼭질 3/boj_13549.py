from collections import deque
import math
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [math.inf for _ in range(500001)]

result = math.inf
queue = deque([(N, 0)])
visited[N] = 1
while queue:
  src, time = queue.popleft()
  if src == K:
    result = min(result, time)
  if time < result:
    plus, minus, mul = src+1, src-1, src*2
    if 0 <= plus < 500001 and visited[plus] > time:
      visited[plus] = time+1
      queue.append((plus, time+1))
    if 0 <= minus < 500001 and visited[minus] > time:
      visited[minus] = time+1
      queue.append((minus, time+1))
    if 0 <= mul < 500001 and visited[mul] > time:
      visited[mul] = time
      queue.append((mul, time))