"""
날짜 : 2023.01.13
이름 : 백현조
내용 : 파이썬 사용자 관리 프로그램 실습하기
"""

import pymysql
conn = pymysql.connect(host='127.0.0.1',
                 user='root',
                 password='1234', 
                 db='java1db', 
                 charset='utf8')



while True:
    print('0: 종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except Exception as e:
        print('다시 입력하세요.' , e)
        continue

    if answer == 0:
        break
    elif answer == 1 :
        data = list(input('아이디, 비번, 이름, 휴대폰, 나이 순으로 입력 :').split())
        cur = conn.cursor()
        sql = "insert into `user1` values ('%s','%s','%s','%s','%s')"
        cur.execute(sql % (data[0],data[1],data[2],data[3],data[4]))
        conn.commit()

        print('등록완료')
    elif answer == 2 :
        sql = "select * from `user1` "
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print(' |아이디|비밀번호|이름|휴대폰|나이')
        for row in cur.fetchall():
            print('-o-o-o-o-o-o-o-o-o-o-o-o-')
            print('|%s|%s|%s|%s|%s|'% (row[0], row[1], row[2], row[3], row[4]) )
        print('조회완료')

    elif answer == 3 :
        data2 = (input('이름 입력 :'))
        cur = conn.cursor()
        sql = "select * from `user1` where `name` = '{}' ".format(data2)
        
        cur.execute(sql)
        conn.commit()
        print(' |아이디|비밀번호|이름|휴대폰|나이')
        for row in cur.fetchall():
            print('|%s|%s|%s|%s|%s|'% (row[0], row[1], row[2], row[3], row[4]) )

        print('검색완료...')
        

    elif answer == 4 :
        data = (input('삭제할 아이디 입력 :'))
        cur = conn.cursor()
        sql = "delete from `user1` where `uid`='%s'"
        cur.execute(sql%data)

        conn.commit()
    else:
        print('0 ~ 4 까지만 입력하시오.')
        

   




#데이터베이스 종료
conn.close()
print('프로그램 종료')

