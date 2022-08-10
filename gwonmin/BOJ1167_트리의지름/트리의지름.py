import sys
from collections import deque

input = sys.stdin.readline
v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v):
    temp = deque(map(int,input().split()))
    node_idx = temp.popleft()
    while temp:
        if temp[0] == -1:
            break
        node = temp.popleft()
        dist = temp.popleft()
        graph[node_idx].append((node,dist))

def bfs(start):
    visit = deque()
    visit.append((start, 0))
    visited = [0 for _ in range(len(graph))]
    visited[start] = 1

    max_dist = 0
    max_idx = start

    while visit:
        now_idx,now_dist = visit.popleft()

        if max_dist < now_dist:
            max_dist = now_dist
            max_idx = now_idx

        for node,dist in graph[now_idx]:
            if visited[node] == 0:
                visit.append((node, now_dist + dist))
                visited[node] = 1
    return max_idx, max_dist

# 임의의 한 점에서 BFS 알고리즘을 이용하여 각 노드까지의 거리를 구하고, 이 중 최대 거리를 갖는 노드에서 시작하여
# 다시 한번 각 노드까지의 최대 거리를 구한다면 그 최대 거리가 트리의 지름이 된다.
temp_idx, temp_max = bfs(1)
final_idx, final_max = bfs(temp_idx)
print(final_max)