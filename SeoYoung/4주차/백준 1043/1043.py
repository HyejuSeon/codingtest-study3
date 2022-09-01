# 어떤 사람이 어떤 파티에서는 진실을 듣고, 또 다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다

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