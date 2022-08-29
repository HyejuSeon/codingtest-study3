from collections import deque
import sys

n,k=map(int, sys.stdin.readline().strip().split())

dx=[-1, 0, 1]
q=deque()
visited=[-1 for _ in range(100001)]
q.append(n)
visited[n]=0

def bfs():
    while q:
        x=q.popleft()
        if x==k:
            print(visited[x])
            return
        for i in range(3):
            if dx[i]==0:
                nx=x*2
                if 0<=nx<100001 and visited[nx]==-1:
                    q.appendleft(nx)  # 우선순위 고려 왼쪽에 추가
                    visited[nx]=visited[x]
            else:
                nx=x+dx[i]
                if 0<=nx<100001 and visited[nx]==-1:
                    q.append(nx)
                    visited[nx]=visited[x]+1

bfs()