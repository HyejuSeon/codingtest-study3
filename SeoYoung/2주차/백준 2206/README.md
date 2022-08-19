## 백준 2206 벽 부수고 이동하기

### 알고리즘

```txt
 ✅ BFS
```

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,isCrash):
    q=deque()
    q.append((x,y,isCrash))
    visited[x][y][isCrash]=1

    while q:
        cur_x,cur_y,isCrash=q.popleft()

        if cur_x==n-1 and cur_y==m-1:
            return visited[cur_x][cur_y][isCrash]
        for i in range(4):
            nx=cur_x+dx[i]
            ny=cur_y+dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            # 벽이 없고 아직 방문하지 않은 경우 벽 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][isCrash] == 0:
                q.append((nx, ny, isCrash))
                visited[nx][ny][isCrash] = visited[cur_x][cur_y][isCrash] + 1
            # 벽이 있고 벽을 아직 부수지 않은 경우 벽 부수고 이동
            if graph[nx][ny] == 1 and isCrash == 0:
                q.append((nx, ny, isCrash + 1))
                visited[nx][ny][isCrash + 1] = visited[cur_x][cur_y][isCrash] + 1
    return -1

print(bfs(0,0,0))
```
