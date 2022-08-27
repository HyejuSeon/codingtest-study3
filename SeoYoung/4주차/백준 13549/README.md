## 백준 13549 숨바꼭질 3

### 알고리즘

```txt
 ✅ bfs
```

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

def bfs(v):
    queue=deque([v])
    dis[v]=0

    while queue:
        v=queue.popleft()

        if v==k:
            print(dis[v])
            break

        for i in (v-1, v+1, v*2):
            if 0<=i<=100000 and dis[i]==-1:
                if i==v*2:
                    # 순간이동은 0초 걸림
                    dis[i]=dis[v]
                    # 순간이동이 훨씬 시간이 적게 걸리므로 큐의 앞에 넣어서 우선순위를 높임
                    queue.appendleft(i)
                else:
                    dis[i]=dis[v]+1
                    queue.append(i)

n,k=map(int, input().split())
dis=[-1]*100001
bfs(n)
```
