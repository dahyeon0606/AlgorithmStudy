import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
array=list(map(int,input().split()))
array.sort() #오름차순 정렬
a=array.pop() #가장 큰 값
b=array.pop() #두번째로 큰 값

aCount=m//(k+1)*k
aCount+=m%(k+1)
bCount=m-aCount

answer=a*aCount+b*bCount
print(answer)