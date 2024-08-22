import sys

n=int(input())

dic={"BANANA":0,
     "STRAWBERRY":0,
     "LIME":0,
     "PLUM":0}

for _ in range(n):
    fruit,count=map(str,input().split())
    dic[fruit]+=int(count)
# print(dic)

answer=[]
for v in dic.values():
    # if v>5:
    #     print("NO")
    #     sys.exit()
    if v==5:
        answer.append(1)
    else:
        answer.append(0)


if 1 in answer:
    print('YES')
else:
    print('NO')