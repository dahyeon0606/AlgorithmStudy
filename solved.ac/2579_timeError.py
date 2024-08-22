import sys
input=sys.stdin.readline
import itertools

n=int(input())
stair=[0]

for _ in range(n):
    stair.append(int(input()))

maxAnswer=0

for i in range(n+1): #1단, 2단씩 몇칸 올라가야 하는지 구하기
    for j in range(n+1):
        oneTwoCount=1*i+2*j
        if oneTwoCount==n:
            oneTwoList=[]
            for _ in range(i): # 1과 2로 이루어진 리스트 만들기
                oneTwoList.append(1)
            for _ in range(j):
                oneTwoList.append(2)
            
            per=set(itertools.permutations(oneTwoList)) #가능한 모든 순열 구하기
            for oneTwoLists in per:
                for o in range(2,len(oneTwoLists)): #1,1,1 혹은 2,1,1 이면 패스
                    if oneTwoLists[o]==1 and oneTwoLists[o-1]==1 and oneTwoLists[o-2]==1:
                        break
                    if oneTwoLists[o]==1 and oneTwoLists[o-1]==1 and oneTwoLists[0-2]==1:
                        break
                else: #그게 아니면 계단의 점수 합 구하기
                    sum=0
                    start=0
                    for k in oneTwoLists:
                        start+=k
                        sum+=stair[start]
                    maxAnswer=max(sum,maxAnswer)

print(maxAnswer)