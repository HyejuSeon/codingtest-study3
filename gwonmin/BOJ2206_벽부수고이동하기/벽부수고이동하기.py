import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

def bfs(start):
    visit = deque()
    visit.append(start)
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]][start[2]] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while visit:
        x, y, z = visit.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny][z] == 0 and graph[nx][ny] != '1':
                    visit.append([nx,ny,z])
                    visited[nx][ny][z] = visited[x][y][z] + 1

                # 벽을 아직 부수지 않은 경우
                elif graph[nx][ny] == '1' and z == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    visit.append([nx,ny,z+1])

    return -1

print(bfs([0,0,0]))

