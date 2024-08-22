import sys

n=int(input())
line=[]
for _ in range(n):
    line.append(int(input()))

if n==1:
    print(0)
    sys.exit()

count=0
dasom=line.pop(0)

while dasom<=max(line): #더 큰 값이 존재하는 동안 반복
    line.sort(reverse=True) #득표 수가 큰 것부터 정렬

    for i in range(len(line)):
        if dasom<=line[i]: #더 크거나 같으면 표 뺃어오기
            dasom+=1
            line[i]-=1
            count+=1

            break #가장 큰 수부터 빼기 위해서 한번 큰 수 빼면 반복 끝내기
print(count)