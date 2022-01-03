#모듈 임포트
import pymysql

#DB연결
conn = pymysql.connect(host='localhost', user='kosmo_user', 
    password='1234', db='kosmo_db', charset='utf8')

#커서생성
curs = conn.cursor()
sql = f"""INSERT INTO board (title, content, id) 
    VALUES ('{input('제목:')}', '{input('내용:')}', 'kosmo')"""

try:
    curs.execute(sql)
    conn.commit()
    print("1개의 레코드가 입력됨")
except Exception as e:
    conn.rollback()
    print("쿼리 실행시 오류발생", e)
    
conn.close()