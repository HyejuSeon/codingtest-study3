## 백준 11053 가장 긴 증가하는 부분 수열

### 알고리즘

```txt
 ✅ dp
```

### 코드 구현

사용 언어 : **파이썬**

```python
n=int(input())
seq=list(map(int,input().split()))
dp=[0]*n

for i in range(n):
    # 0 ~ i-1번째 인덱스 사이에서 가장 큰 수열을 구해서 그 길이에 +1하는 원리
    for j in range(i):
        # dp[i]<dp[j]는 '가장 긴' 수열의 길이를 저장하기 위해 필요한 조건
        if seq[i]>seq[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))
```
