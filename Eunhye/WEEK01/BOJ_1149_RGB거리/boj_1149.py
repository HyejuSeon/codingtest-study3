N = int(input())
costs = [ list(map(int, input().split())) for _ in range(N) ]
cache = [[0 for _ in range(3)] for _ in range(1000)]
cache[0][0] = costs[0][0]
cache[0][1] = costs[0][1]
cache[0][2] = costs[0][2]

for i in range(1, N):
    cache[i][0] = costs[i][0] + min(cache[i-1][1], cache[i-1][2])    
    cache[i][1] = costs[i][1] + min(cache[i-1][0], cache[i-1][2])    
    cache[i][2] = costs[i][2] + min(cache[i-1][0], cache[i-1][1])   

print(min(cache[N-1])) 