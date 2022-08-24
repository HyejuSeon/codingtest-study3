## 백준 11660 구간 합 구하기 5

### 알고리즘

```txt
 ✅ dp
 ✅ sys.stdin.readline 안쓰면 시간초과 남
```

### 코드 구현

사용 언어 : **파이썬**

```python
import sys
input = sys.stdin.readline

n,m=map(int,input().split())

graph = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + list(map(int,input().split()))
    graph.append(nums)

# grpah[i][j]에는 [0][0]부터 [i][j]까지의 누적합이 각각 더해져 있도록 할 것
# 행 별로 더하기
for i in range(1,n+1):
    for j in range(1,n):
        graph[i][j+1]+=graph[i][j]

# 열 별로 더하기
for j in range(1,n+1):
    for i in range(1,n):
        graph[i+1][j]+=graph[i][j]

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(graph[x2][y2]-graph[x1-1][y2]-graph[x2][y1-1]+graph[x1-1][y1-1])

```
