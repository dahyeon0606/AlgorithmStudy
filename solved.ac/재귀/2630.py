import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

paper=[]
n=int(input())
for _ in range(n):
    paper.append(list(map(int,input().split())))

white=0
blue=0


def cut(slice):
    global white,blue

    if len(slice)==1:
        if slice[0][0]==0:
            white+=1
        else:
            blue+=1
        return
    
    check=True
    temp=slice[0][0]
    for i in range(len(slice)):
        for j in range(len(slice)):
            if slice[i][j]!=temp:
                check=False

    if check==True:
        if temp == 0:
            white+= 1
        else:
            blue+= 1
        return
    
    n=len(slice)//2
    cut([row[:n] for row in slice[:n]])
    cut([row[:n] for row in slice[n:]])
    cut([row[n:] for row in slice[:n]])
    cut([row[n:] for row in slice[n:]])

cut(paper)
print(white)
print(blue)