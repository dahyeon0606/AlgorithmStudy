import sys
input=sys.stdin.readline

n,m=map(int,input().split())

my_dic={}

for _ in range(n): #O(n)
    site,pwd=input().strip().split()
    my_dic[site]=pwd

answer=[]
for _ in range(m): #O(m)
    site=input().strip()
    answer.append(my_dic[site])

for a in answer: #O(m) answer에 들어갈 수 있는 최대 길이는 비밀번호를 찾으려는 사이트의 개수 m
    print(a)

##### O(n or m) = O(100,000)