## 백준 1504 특별한 최단 경로

### 알고리즘

```txt
 ✅ 다익스트라
```

### 코드 구현

사용 언어 : **파이썬**

```python
import heapq
INF=int(1e9)

def dijkstra(start):
    q=[]
    distance=[INF]*(n+1)

    heapq.heappush(q, (0,start))
    distance[start]=0

    while q:
        dis,v=heapq.heappop(q)

        if distance[v]<dis:
            continue

        for idx, cost in roads[v]:
            c=dis+cost

            if distance[idx]>c:
                distance[idx]=c
                heapq.heappush(q, (c, idx))

    return distance

n,e=map(int,input().split())
roads=[[] for _ in range(n+1)]

for i in range(e):
    a,b,c=map(int,input().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

v1, v2= map(int,input().split())

start_dis=dijkstra(1)
v1_dis=dijkstra(v1)
v2_dis=dijkstra(v2)
answer=min(start_dis[v1]+v1_dis[v2]+v2_dis[n], start_dis[v2]+v2_dis[v1]+v1_dis[n])
print(answer if answer<INF else -1)
```
