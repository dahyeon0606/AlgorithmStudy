import sys
input=sys.stdin.readline

n=int(input())
papers=[]
for _ in range(n):
    papers.append(list(map(int,input().split())))

zero,one,minus=0,0,0
def paperCut(slice_papers):
    global zero,one,minus

    temp=slice_papers[0][0]
    for slice_paper in slice_papers: #행씩
        if any(temp!=row for row in slice_paper): #행에 속한 열씩
            n=len(slice_papers)//3
            n2=n*2
            paperCut([row[:n] for row in slice_papers[:n]])
            paperCut([row[n:n2] for row in slice_papers[:n]])
            paperCut([row[n2:] for row in slice_papers[:n]])

            paperCut([row[:n] for row in slice_papers[n:n2]])
            paperCut([row[n:n2] for row in slice_papers[n:n2]])
            paperCut([row[n2:] for row in slice_papers[n:n2]])

            paperCut([row[:n] for row in slice_papers[n2:]])
            paperCut([row[n:n2] for row in slice_papers[n2:]])
            paperCut([row[n2:] for row in slice_papers[n2:]])

            return

    if temp==0: zero+=1
    elif temp==1: one+=1    
    else: minus+=1

paperCut(papers)
print(minus)
print(zero)
print(one)