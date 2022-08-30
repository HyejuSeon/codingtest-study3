## 백준 1043 거짓말

### 알고리즘

```txt
 ✅ set
```

### 코드 구현

사용 언어 : **파이썬**

```python
n,m=map(int,input().split())
truth=set(input().split()[1:])
parties=[]

for _ in range(m):
    parties.append(set(input().split()[1:]))

# 한번의 턴으로 truth가 갱신되면 갱신된 truth 집합에 따라 또 진실을 들은 사람을 확인해야 하므로
# 파티의 수만큼 반복해서 확인해야 한다.
for _ in range(m):
    for party in parties:
        if truth.intersection(party):
            truth=truth.union(party)

answer=0
for party in parties:
    if truth.intersection(party):
        continue
    answer+=1

print(answer)
```
