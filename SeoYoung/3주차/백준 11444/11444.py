# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고 1번째 피보나치 수는 1이다.
# 0 -> 1 -> 0+1=1 -> 1+1=2 -> ...
# n이 주어졌을 때 n번째 피보나치 수를 구하는 프로그램을 작성하시오
# 행렬을 이용한 방법으로 풀어야 함

import sys
c = 1000000007

# 행렬의 곱셈함수
def multi(m1, m2): 
    ans=[]
    for i in range(len(m1)):
        ans.append([])
        for j in range(len(m2[0])):
            temp=0
            for k in range(len(m1[0])):
                temp+=m1[i][k]*m2[k][j]
            ans[i].append(temp%c)
    return ans

# 행렬의 거듭제곱 함수
def power(m, p):
    if p==1:
        return m
    else:
        temp=power(m, p//2)
        if p%2==0:
            return multi(temp, temp)
        else:
            return multi(multi(temp, temp), m)

init=[[1,1],[1,0]]
n=int(sys.stdin.readline())
print(power(init,n)[0][1])

