## 백준 11404 플로이드

### 알고리즘

```txt
 ✅ 플로이드 워셜 알고리즘
```

### 코드 구현

사용 언어 : **파이썬**

```python
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
```
