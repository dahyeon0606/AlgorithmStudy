import sys
input=sys.stdin.readline

def akaraka(s):
    global answer

    #문자열의 길이가 1이 될때까지 재귀가 깊어져야 아카라카 펜린드롬
    if len(s)==1: 
        answer="AKARAKA"
        return
    
    #문자열의 길이가 1이 아니라면, 아카라카 펜린드롬인지 검사
    else:
        #펜린드롬 인지 검사, 펜린드롬이 아닐경우 더이상 재귀를 반복할 필요가 없으므로 종료
        if s != s[::-1]:
            return
        
        #아카라카 펜린드롬인지 검사
        else:
            N=len(s)//2 
            akaraka(s[:N]) #왼쪽 문자열 슬라이싱
            akaraka(s[-N:]) #오른쪽 문자열 슬라이싱

S=input().strip() #줄바꿈때문에 펜린드롬 검사에서 오류가 남
answer="IPSELENTI"
akaraka(S)
print(answer)
