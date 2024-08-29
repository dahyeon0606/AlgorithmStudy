import sys
input=sys.stdin.readline

n,m=map(int,input().split())
money=[]
for _ in range(n):
    money.append(int(input()))

dp=[10001]*(m+1)
dp[0]=0

###############최적화 부분#####################
for i in range(n):
    for j in range(money[i],m+1): 
        dp[j]=min(dp[j],dp[j-money[i]]+1)
###############최적화 부분#####################

if dp[m]!=10001:
    print(dp[m])
else:
    print(-1)