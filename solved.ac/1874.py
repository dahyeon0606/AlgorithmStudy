import sys
input=sys.stdin.readline

n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

stack=[0,1]
count=1
answer=['+']
for i in range(n):   
    while stack[-1]<nums[i] or stack[-1]==0:
        count+=1
        stack.append(count)
        answer.append('+')
    if stack[-1]==nums[i]:
        stack.pop()
        answer.append('-')

if stack[-1]==0:
    for a in answer:
        print(a)
else:
    print('NO')