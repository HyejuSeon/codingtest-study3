N=int(input())
dp=[list(map(int, input().split())) for i in range(N)]

for i in range(1, N):
    for j in range(3):
        if j==0: 
            dp[i][0]+=min(dp[i-1][1], dp[i-1][2])
        elif j==1:
            dp[i][1]+=min(dp[i-1][0], dp[i-1][2])
        elif j==2:
            dp[i][2]+=min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))
