
import sys
input=sys.stdin.readline

n=int(input())
house=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    house.append(temp)

dp=[[0,0,0] for _ in range(1001)]
dp[0][0]=house[0][0] #red
dp[0][1]=house[0][1] #green
dp[0][2]=house[0][2] #blue

for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+house[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+house[i][1]
    dp[i][2]=min(dp[i-1][1],dp[i-1][0])+house[i][2]
print(min(dp[n-1]))