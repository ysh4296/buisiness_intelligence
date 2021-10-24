#DBConnect.py

import pymysql
import pandas as pd

def insertDB(dataDic):
    if '음식점이름' in dataDic.keys():
        R_name = dataDic['음식점이름']
    else:
        R_name = None

    if '유저이름' in dataDic.keys():
        U_name = dataDic['유저이름']
    else:
        U_name = None

    if '유저평가' in dataDic.keys():
        U_rate = dataDic['유저평가']
    else:
        U_rate = None
    print("hi")
    try:
        conn = pymysql.connect(host='localhost', user='root', password='dbtmdgns1345', port=3306, db='Review', charset='utf8')
        if not conn.open:
            print("연결 실패")
        if conn.open:
            print("연결 성공")
        with conn.cursor() as cursor:
            sql = "INSERT INTO Reviews (R_name, U_name , U_rate) VALUES (%s, %s, %s)"
            print(R_name,"  ", U_name ,"  ", U_rate)
            cursor.execute(sql, (R_name, U_name, U_rate))
            conn.commit()
    finally:
        conn.close()