import sys
input=sys.stdin.readline

n,m=map(int,input().split())
answer=0
for i in range(n):
    card=list(map(int,input().split()))
    minValue=min(card)
    answer=max(minValue,answer)
print(answer)