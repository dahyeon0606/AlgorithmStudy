import sys
input=sys.stdin.readline
import itertools

while(True):
    temp=list(map(int,input().split()))
    n=temp[0]
    if n==0: break
    nums=temp[1:]

    numsPrint=itertools.permutations(nums,6) #6개로 가능한 순열 리스트
    for num in numsPrint: #각 순열을 출력
        if list(num)==sorted(num): #순열이 정렬되어 있을 경우만
            print(" ".join(map(str,num)))  #공백으로 구분하여 순열을 출력 
    print()
        