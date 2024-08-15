
import sys
input=sys.stdin.readline

#bottom-up
dp=[0]*(10**6+1)
n=int(input())
for i in range(2,n+1):
    dp[i]=dp[i-1]+1 #1을 빼고(이때의 카운트) + 카운트+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1) #2로 나누고(이때의 카운트) + 카운트+1 , -1 했을때가 최소인지 /2 했을때가 최소 인지 비교
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1) #3으로 나누고(이때의 카운트) + 카운트+1
print(dp[n])