import sys
input=sys.stdin.readline

n=int(input())
stair=[0]

for _ in range(n):
    stair.append(int(input()))

if n==1: #계단이 하나면 점수 출력하고 시스템 종료
    print(stair[1])
    sys.exit()

dp=[0]*(n+1)
dp[1]=stair[1] #1단 올랐을 때 최대 점수
dp[2]=stair[1]+stair[2] #2단 올랐을 때 최대 점수

for i in range(3,n+1):
    dp[i]=max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
print(dp[n])