"""
https://www.acmicpc.net/step/1
 날짜 : 2023.01.02
 이름 : 백현조
 내용 : 백준 1단계 (2588)
        11번 - 나머지 
"""
num1 = int(input())
num2 = input()

result1 = num1 * int(num2[2])
result2 = num1 * int(num2[1])
result3 = num1 * int(num2[0])
result4 = num1 * int(num2)

print(result1)
print(result2)
print(result3)
print(result4)

