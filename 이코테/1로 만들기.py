import sys

x=int(input())
dp=[0]*(x+1)

dp[1]=0
if x==1:
    print(dp[1])
    sys.exit()
dp[2]=1

for i in range(3,x+1):
    temp1=temp2=temp3=temp4=10**8
    if i%5==0:
        temp1=dp[i//5]+1
    if i%3==0:
        temp2=dp[i//3]+1
    if i%2==0:
        temp3=dp[i//2]+1
    temp4=dp[i-1]+1
    dp[i]=min(temp1,temp2,temp3,temp4)
print(dp[x])