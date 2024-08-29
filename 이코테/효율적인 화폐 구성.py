
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
money=[]
for _ in range(n):
    money.append(int(input()))

dp=[10001]*(m+1)
dp[0]=0

for i in range(1,m+1):
    temp=[]
    for j in range(n):
        if i-money[j]<0:
            temp.append(10001)
        else:
            temp.append(dp[i-money[j]]+1)
    dp[i]=min(temp)
if dp[m]!=10001:
    print(dp[m])
else:
    print(-1)