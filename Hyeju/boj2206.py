# 벽 부수고 이동하기
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][w]:
                if not mat[nx][ny]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))
                elif mat[nx][ny] and not w:
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    q.append((nx, ny, 1))
    return -1

print(bfs())
