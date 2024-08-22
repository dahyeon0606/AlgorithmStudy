
#n: 도감 포켓몬 갯수, m: 맞춰야 하는 문제 갯수 1<=n,m<=100,000
# n개가 입력으로 들어온 후, m개가 주어지면 출력
# 숫자가 입력 -> 포켓몬 이름 출력 / 포켓몬 이름 입력 -> 숫자가 출력

import sys
input=sys.stdin.readline

dicNum={}
dicName={}
n,m=map(int,input().split())

for i in range(1,n+1): #도감 저장 O(n)
    name=input().strip()
    dicNum[i]=name
    dicName[name]=i


for j in range(m): #O(m)
    quiz=input().strip()

    try:
        intQuiz=int(quiz)
    except ValueError as v:
        print(dicName[quiz])
    else:
        print(dicNum[intQuiz])

### O(n)+O(m) O(200,000)

