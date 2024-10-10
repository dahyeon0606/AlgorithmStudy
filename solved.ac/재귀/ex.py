import sys
input=sys.stdin.readline

n=int(input())
papers=[]
for _ in range(n):
    papers.append(list(map(int,input().split())))
print(papers)