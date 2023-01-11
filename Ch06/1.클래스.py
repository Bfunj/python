"""
날짜 : 2023.01.11
이름 : 백현조
내용 : 파이썬 클래스 실습하기
"""

from sub1.car import Car
from sub1.Account import Account 

bmw = Car('BMW', '검정색', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

sonata = Car('소나타', '흰색', 3000)

sonata.speedUp()
sonata.speedDown()
sonata.show()


kb= Account('국민은행', '10-1115','김유신',100000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

