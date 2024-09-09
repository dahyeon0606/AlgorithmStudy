import sys
input=sys.stdin.readline

n=int(input())
trianle=[]
for _ in range(n):
    trianle.append(list(map(int,input().split())))

dp=[[0 for _ in range(501)] for _ in range(501)]
dp[0][0]=trianle[0][0]

for i in range(1,n): #O(n*n) = O(2500)
    for j in range(i+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+trianle[i][j]
print(max(dp[n-1])) #O(500)