from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(n)]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,isCrash):
    #isCrash 0 : 벽 안부시고 가는 경우, 1: 부신 경우
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
            # 벽 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][isCrash] == 0:
                q.append((nx, ny, isCrash))
                visited[nx][ny][isCrash] = visited[cur_x][cur_y][isCrash] + 1
            # 벽 부수고 이동
            if graph[nx][ny] == 1 and isCrash == 0:
                q.append((nx, ny, isCrash + 1))
                visited[nx][ny][isCrash + 1] = visited[cur_x][cur_y][isCrash] + 1
    return -1

print(bfs(0,0,0))


