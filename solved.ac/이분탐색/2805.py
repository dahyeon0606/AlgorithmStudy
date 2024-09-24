import sys
input=sys.stdin.readline

N,M=map(int,input().split()) #나무 N개, 가져갈 나무 M미터
trees=list(map(int,input().split())) #나무들의 높이

answer=0 #최대로 자를 수 있는 높이 H
start=1 #절단기에 설정할 수 있는 최소 높이
end=max(trees)-1 #O(10**6) #절단기에 설정할 수 있는 최대 높이 => start ~ end 높이 만큼 절단기 설정 가능

#이분 탐색
while start<=end: #O(log2*10**9)
    mid=(start+end)//2
    temp=0 #절단기로 잘려나간 부분의 합을 저장할 변수
    for tree in trees: #O(10**6)
        if mid<tree: #나무를 자를 수 있을 경우만
            temp+=tree-mid
    if temp>=M: #잘려나간 부분이 너무 많은 경우, 더 높게 자르기
        start=mid+1
        answer=mid
    else: #잘려나간 부분이 너무 적은 경우, 더 낮게 자르기
        end=mid-1
print(answer)

####O(10**6 log 2*10**9) = O(3*10**7)