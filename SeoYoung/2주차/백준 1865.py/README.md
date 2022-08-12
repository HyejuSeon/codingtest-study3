## 백준 1865 웜홀

### 알고리즘

```txt
 ✅ 벨만포드 알고리즘
 - 한 노드에서 다른 노드까지의 최단거리를 구하는 알고리즘
 - 음수 간선이 있어도 최적의 해를 찾을 수 있음 ( 음수 간선의 순환을 감지할 수 있음 )
 - 간선에 음수가 포함되어 있으면 벨만포드 사용해야함
```

### 코드 구현

사용 언어 : **파이썬**

```python
INF=int(1e9)

def bf(start):
    # 최단거리 테이블 초기화
    dis=[INF]*(n+1)
    dis[start]=0

    # 정점개수만큼(n-1만큼) 반복
    for i in range(n):
        for cur,next,cost in graph:
            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[next]>cost+dis[cur]:
                dis[next]=cost+dis[cur]
                # n번째 루프에서도 값이 갱신되면 음수 순환이 존재한다는 것
                if i==n-1:
                    return True

    return False



tc=int(input())

for _ in range(tc):
    n,m,w= map(int, input().split())
    graph=[]

    for _ in range(m):
        s,e,t=map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s,e,t=map(int,input().split())
        graph.append((s,e,-t))

    isPossible=bf(1)
    if isPossible:
        print("YES")
    else:
        print("NO")

```
