## 풀이  

combinations 모듈을 사용하여 풀어주었습니다.  

N, M을 입력받고, 1부터 N까지의 수열을 M크기 만큼의 combination을 구해주어 출력해줍니다.  

## 코드  
```python
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
for combi in combinations(range(1, N+1), M):
  print(*combi, sep=" ")
```