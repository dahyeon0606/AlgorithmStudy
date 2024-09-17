import sys
input=sys.stdin.readline


n,m,k=map(int,input().split())
array=list(map(int,input().split()))
array.sort() #오름차순 정렬
a=array.pop() #가장 큰 값
b=array.pop() #두번째로 큰 값

answer=0
count=0

while count<m:
    for _ in range(k):
        if count<m:
            answer+=a
            count+=1
    if count<m:
        answer+=b
        count+=1
print(answer)
