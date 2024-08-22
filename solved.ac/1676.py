
# 10 9 8 7 6 5 4 3 2 1
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수

n=int(input())

def facto(n):
    sum=1
    for i in range(n,1,-1):
        sum*=i
    return sum

f=list(str(facto(n)))
f.reverse()

count=0
if f[0]=='0':
    count+=1
for i in range(1,len(f)):
    if f[i]=='0':
        count+=1
    elif f[i-1]=='0' and f[i]!='0':
        break  
print(count)