import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input()) #의상 수
    kinds={}
    for _ in range(n):
        name,kind=input().split()
        if kind in kinds:
            kinds[kind]+=1
        else:
            kinds[kind]=1

    answer=1
    for count in kinds.values():
        answer*=count+1 #안 쓴 걸 더함 예) a쓴거, b쓴거, 아무것도 안 쓴거
    answer-=1
    print(answer)