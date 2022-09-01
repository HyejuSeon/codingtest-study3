## 백준 1238 파티

### 알고리즘

```txt
 ✅ 다익스트라
```

### 코드 구현

사용 언어 : **파이썬**

```python
import heapq

INF=int(1e9)

n,m,x=map(int,input().split())
roads=[[] for _ in range(n+1)]

for i in range(m):
    a,b,dis=map(int,input().split())
    roads[a].append((b,dis))

def dijkstra(start):
    q=[]
    distance=[INF] * (n+1)

    #초기화
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        # start->v : dis
        dis,v=heapq.heappop(q)

        # 이미 distance 배열에 dis보다 작은 값이 저장되어 있다면 갱신 필요 x
        if distance[v]<dis:
            continue

        # v->idx: cost
        for idx, cost in roads[v]:
            # c=dis(start->v)+cost(v->idx) : start->idx 비용
            c=dis+cost

            # distacne에 저장된 값이 c보다 크면 새로운 값으로 갱신
            if distance[idx]>c:
                distance[idx]=c
                heapq.heappush(q, (c, idx))

    return distance

answer=0
for i in range(1, n+1):
    homeToParty=dijkstra(i)
    PartyToHome=dijkstra(x)
    answer=max(answer, homeToParty[x]+PartyToHome[i])

print(answer)
```
