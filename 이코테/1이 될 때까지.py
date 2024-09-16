import sys
input=sys.stdin.readline

n,k=map(int,input().split())
dp=[0]*100001
dp[2]=1

for i in range(3,n+1):
    dp[i]=dp[i-1]+1
    if i%k==0:
        dp[i]=min(dp[i],dp[i//k]+1)
print(dp[n])