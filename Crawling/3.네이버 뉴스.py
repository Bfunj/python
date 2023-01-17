"""
    날짜 : 2023.01.16
    이름 : 백현조
    내용 : 파이썬 네이버 뉴스 파싱 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

# 엑셀파일 생성
Workbook  = Workbook()
sheet = Workbook.active



pg=1
count=1
while True:
    # html 요청

    url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230&page=%d' %pg
    html=req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

    #print(html)

    # 문서객체 생성
    dom = bs(html, 'html.parser')
    tit=dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
    test=dom.select_one('#main_content > div.paging > strong').text
    
    if int (pg) >int (test) :
        break

    print('tit : ',tit)
    print('test : ',test)

    lis=dom.select('#main_content > div.list_body.newsflash_body > ul > li')

    for li in lis:
        tag_a=li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        href=tag_a['href']

        sheet.append([count, title.strip(), href.strip()])
        print('%d건 저장..' % count)
        #print('count : ',count)
        #print('title : ', title.strip())
        #print('link : ', href.strip())

        count += 1

    pg += 1

    
Workbook.save('C:/Users/java1/Desktop/News.xlsx')
Workbook.close()

print('프로그램 종료..')