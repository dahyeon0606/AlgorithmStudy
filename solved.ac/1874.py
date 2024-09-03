import sys
input=sys.stdin.readline

n=int(input())
nums=[] #수열
for _ in range(n):
    nums.append(int(input()))

stack=[0]
count=0 #스택에 삽입할 수 1~n 
answer=[]
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