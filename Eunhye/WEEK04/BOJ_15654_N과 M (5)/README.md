## 풀이  

permutations 모듈을 사용하여 풀어주었습니다.  

N, M을 입력받고, 입력 받은 수열을 정렬해준 뒤 해당 수열에서 M크기 만큼의 permutation을 구해주어 출력해줍니다.  

## 코드  
```python
from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
seq = sorted(map(int, input().split()))
for permu in permutations(seq, M):
  print(*permu, sep=" ")
```