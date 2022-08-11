## 백준 1149 RGB거리

### 알고리즘

```txt
 ✅ 동적계획법 DP
```

### 코드 구현

사용 언어 : **파이썬**

```python
N=int(input())
dp=[list(map(int, input().split())) for i in range(N)]

# i번째 집과 i-1번째 집의 색은 겹치지 않아야 함
# i번째 집의 색깔을 제외한 나머지 색 중에서 i-1번째 집을 칠하는 비용이 적은 것을 현재 집 색에 더해줘서 비용을 계산함
# 모든 집을 계산 완료 후 dp[N] 중 최솟값을 구하면 그게 답!
for i in range(1, N):
    for j in range(3):
        if j==0:
            dp[i][0]+=min(dp[i-1][1], dp[i-1][2])
        elif j==1:
            dp[i][1]+=min(dp[i-1][0], dp[i-1][2])
        elif j==2:
            dp[i][2]+=min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))

```
