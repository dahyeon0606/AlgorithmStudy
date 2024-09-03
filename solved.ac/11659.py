import sys
input=sys.stdin.readline

n,m=map(int,input().split())
nums=list(map(int,input().split()))
for i in range(1,n): #O(100,000) 누적합 구하기
    nums[i]+=nums[i-1]

answer=[]

for _ in range(m):
    i,j=map(int,input().split())
    if i==1:
        answer.append(nums[j-1])
    else:
        answer.append(nums[j-1]-nums[i-2])

for a in answer:
    print(a)