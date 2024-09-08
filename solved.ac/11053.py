import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

dp=[0 for _ in range(1001)]
dp[0]=1

for i in range(1,n):
    for j in range(i):
        if A[i]>A[j]:     
            dp[i]=max(dp[i],dp[j])
    dp[i]+=1
print(max(dp))