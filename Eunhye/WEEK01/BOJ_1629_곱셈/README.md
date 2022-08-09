## 풀이  

보통 power 함수를 재귀로 구현할 때는 지수를 1씩 감소하며 구현해주는 데, 그럴 경우 지수만큼의 재귀호출을 하게 됩니다.  

그러나 여기서 지수를 2로 나눠주며 반절의 값 half를 구해준 뒤, 지수가 짝수일 때는 그저 half를 두 번 곱해주고 홀수일 때는 n을 한 번 더 곱해주면 좀 더 적은 재귀호출로 빠르게 원하는 수를 구할 수 있게 됩니다. 

## 코드  
```python
def power(n, exp):
    if exp == 0:
        return 1
    half = power(n, exp // 2)
    if exp % 2:
        return (half*half*n)%C
    return (half*half)%C
A, B, C = map(int, input().split())
print(power(A, B))
```