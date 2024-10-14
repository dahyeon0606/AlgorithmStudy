#음수로 돌아가는 경우가 생길 수 있는데 이를 구하지 못함

import sys
input=sys.stdin.readline


N,K=map(int,input().split())

if K<N:
    print(N-K)
    sys.exit()

dp=[10**5]*(K+1)

dp[N]=0
dp[N+1]=1
for i in range(N+2,K+1): #5 6
    if i%2==0:
        dp[i]=dp[i//2]+1
    dp[i]=min(dp[i],dp[i-1]+1)
print(dp[K])
print(dp)