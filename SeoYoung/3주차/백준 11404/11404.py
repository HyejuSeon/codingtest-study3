# n개의 도시가 있음. 
# 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다
# 각 버스는 한 번 사용할 때 필요한 비용이 있음
# 도시 a에서 b로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오

import sys
INF=sys.maxsize

n=int(input())
m=int(input())
dist=[[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            dist[i][j]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    dist[a][b]=min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1,n+1):
        for j in range(1, n+1):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j]==INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
    





