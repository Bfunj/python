"""
https://www.acmicpc.net/step/1
 날짜 : 2023.01.02
 이름 : 백현조
 내용 : 백준 1단계 (3003)
        9번 - 킹, 퀸, 룩, 비숍, 나이트, 폰 
"""
chess =[1,1,2,2,2,8]
set=list(map(int, input().split()))
for i in range(6):
    print(chess[i]-set[i], end=' ')