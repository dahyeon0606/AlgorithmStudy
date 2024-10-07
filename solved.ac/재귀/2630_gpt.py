import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

paper=[]
n=int(input())
for _ in range(n):
    paper.append(list(map(int,input().split())))

white=0
blue=0


def cut(subPaper):
    global white,blue
    
    first=subPaper[0][0]
    # for i in range(len(subPaper)):
    #     for j in range(len(subPaper)):
    #         if subPaper[i][j]!=first:
    for row in subPaper: #행 반복
        if any(column!=first for column in row): #열 반복, 열이 첫번째 값과 다른지 비교해서 하나라도 True일 때
                n=len(subPaper)//2
                cut([row[:n] for row in subPaper[:n]])
                cut([row[:n] for row in subPaper[n:]])
                cut([row[n:] for row in subPaper[:n]])
                cut([row[n:] for row in subPaper[n:]])
                return #처음 자른 4분할을 마치면 함수 종료
    if first==0:
        white+=1
    else:
        blue+=1

    
    

cut(paper)
print(white)
print(blue)