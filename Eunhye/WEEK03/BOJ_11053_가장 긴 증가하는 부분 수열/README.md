## 풀이

동적계획법으로 풀어주었습니다.  

cache의 format은 다음과 같습니다.  
```
# cache[i]
cache[i]: i index까지의 가장 긴 증가하는 부분 수열의 길이
```  

적어도 자기 자신을 포함하니 1로 초기화해줍니다.  

outer for loop을 N만큼 돌려줍니다. (i) 0 ~ N-1  
inner for loop을 i만큼 돌려줍니다. (j) 0 ~ i-1
 - j는 i보다 작은 index들 입니다.  
 
i번째 수(A\[i\])가 j번째 수(A\[j\])보다 크고(증가하고 있고), i번째의 부분 수열의 길이(cache\[i\])가 j번째의 부분 수열의 길이(cache\[j\])보다 작거나 같을 때 j번째의 부분 수열의 길이(cache\[j\])에 1을 더한 값을 저장해줍니다.

마지막으로 최댓값을 구한 뒤 출력해줍니다.

## 코드

```python
N = int(input())
A = list(map(int, input().split()))
cache = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and cache[i] <= cache[j]:
            cache[i] = cache[j] + 1
print(max(cache))
```