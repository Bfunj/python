"""
    날짜 : 2023.01.17
    이름 : 백현조
    내용 : 파이썬 가상 브라우저 실습하기
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 가상 브라우저

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 가상 브라우저 네이버 이동
browser.get('https://naver.com')

# 로그인 클릭
btnlogin = browser.find_element(By.CSS_SELECTOR, '#account > a')
btnlogin.click()

# 아이디/ 비번 입력
input_id=browser.find_element(By.CSS_SELECTOR, '#id')
input_pw=browser.find_element(By.CSS_SELECTOR, '#pw')

input_id.send_keys('abcd')
input_pw.send_keys('1234')

# 최종 로그인 클릭
btnsubmit = browser.find_element(By.CSS_SELECTOR, '#log\.login')
btnsubmit.click()