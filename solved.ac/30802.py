
n=int(input())
t=list(map(int,input().split()))
T,P=map(int,input().split())

tCount=0
for i in t:
    if i==0: #갯수가 0개일 경우는 카운트 하지 않음
        continue
    elif i<=T:
        tCount+=1
    else:
        a=i//T
        if i%T !=0: #나머지가 0이 아닌 경우에만 1묶음 추가
            a+=1
        tCount+=a

pCount1=n//P
pCount2=n%P

print(tCount)
print(pCount1,pCount2)