import sys
input=sys.stdin.readline

n=int(input())
food=list(map(int,input().split()))

dp=[0]*(100+1)
dp[1]=food[0]
dp[2]=max(dp[1],dp[2])

for i in range(3,n+1):
    dp[i]=max(dp[i-2]+food[i-1],dp[i-1])
print(dp[n])