## 풀이  

예시로 주어진 문자열을 비교하는 표를 만들어보았습니다.  

![BOJ_9251_1](https://user-images.githubusercontent.com/59808674/117243322-fcc15c00-ae71-11eb-82f0-9c360707778a.PNG)  

이 표가 그대로 memoization을 위 한 cache가 됩니다.  

비교하는 문자가 같을 경우 이전의 공통부분(cache\[i-1\]\[j-1\])에 문자를 추가해주어야 합니다. 문자가 같지 않을 경우에는 두 이전 문자열의 공통부분(cache\[i\]\[j-1\], cache\[i-1\]\[j\]) 중 큰 값으로 저장해줍니다.  

## 코드  
```python
import sys

input = sys.stdin.readline

S1, S2 = input().rstrip(), input().rstrip()
N, M = len(S1), len(S2)
cache = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if S1[i-1] == S2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i-1][j], cache[i][j-1])
print(cache[N][M])
```