import sys
input=sys.stdin.readline

video=[]
n=int(input())
for _ in range(n):
    video.append(input().strip())

answer=[]

def videoCheck(videoSlice):
    global answer
    first=videoSlice[0][0]

    for video in videoSlice:
        if any(v!=first for v in video):
            n=len(videoSlice)//2
            answer.append('(')
            videoCheck([row[:n] for row in videoSlice[:n]])
            videoCheck([row[n:] for row in videoSlice[:n]])
            videoCheck([row[:n] for row in videoSlice[n:]])
            videoCheck([row[n:] for row in videoSlice[n:]])
            answer.append(')')
            return
    
    if first=='0':
        answer.append(0)
    else:
         answer.append(1)


videoCheck(video)
for a in answer:
    print(a,end='')
