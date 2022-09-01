# 배당 또한 최대한 가치있게 싸려고 한다. n개의 물건은 무게 w와 가치 v를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 v만큼 즐길 수 있다. 
# 최대 k만큼의 무게만을 넣을 수 있는 배낭만 들고 다닌다고 할 때 준서가 배낭에 넣을 수 있는 물건들의 가치의 최댓값은? 

n,k=map(int,input().split())
stuff=[[0,0]]
dp=[[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    stuff.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=stuff[i][0]
        value=stuff[i][1]

        # 현재 가방 허용 용량(j)이 현재 물건의 무게(weight)보다 작다면 넣지 않는다
        if j<weight:
            dp[i][j]=dp[i-1][j]
        # 그렇지 않다면 현재 넣을 물건의 무게만큼 배당에서 빼고 현재 물건을 넣는다 or 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다
        # 더 가치가 큰 값이 현재 물건의 j번째 인덱스에 저장됨
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[n][k])

