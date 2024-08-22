import sys

def roundUp(x): #round() 대신 오사오입으로 구현한 반올림 함수
    if x-int(x)>=0.5:
        return int(x)+1
    else:
        return int(x)

n=int(input())

if n==0:
    print(0)
    sys.exit()
cut=roundUp(n*0.15)

level=[]
for _ in range(n):
    level.append(int(input())) #O(n)

level.sort() #O(nlogn)

# for _ in range(cut): #cut 번 반복 n*0.15 -> O(n) ==> O(n)*O(n)=O(n**2)
#     level.pop(0) #O(n)
#     level.pop(-1) #O(1)

level=level[cut:n-cut] # ==> O(nlogn)
sum=0
for l in level: #O(n)
    sum+=l

print(roundUp(sum/len(level)))