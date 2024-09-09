import sys
input=sys.stdin.readline

T=int(input())
answer=[]
for _ in range(T):
    n,m=map(int,input().split())
    dp=[[0 for _ in range(30)]for _ in range(30)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1:
                dp[i][j]=j
            elif i==j:
                dp[i][j]=1
            elif i<j:
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
    answer.append(dp[n][m])

for a in answer:
    print(a)        