
import sys
input=sys.stdin.readline

n,m=map(int,input().split())

mySet=set()

for _ in range(n): #O(n)
    temp=input().strip()
    mySet.add(temp)

answer=[]

for _ in range(m): #O(m)
    temp=input().strip()
    if temp in mySet:
        answer.append(temp)

print(len(answer)) #O(1)
answer.sort() #O(nlogn)
for a in answer: #O(n)
    print(a)

##### 가장 큰 시간 복잡도 O(nlogn) = O(500,000 log 500,000) = O(9*10**6)