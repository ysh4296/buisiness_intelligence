#DBConnect.py

import pymysql
import pandas as pd

def insertDBreview(dataDic):
    if '카페이름' in dataDic.keys():
        cafe_name = dataDic['카페이름']
    else:
        cafe_name = None
    if '테마이름' in dataDic.keys():
        thema_name = dataDic['테마이름']
    else:
        thema_name = None
    if '유저이름' in dataDic.keys():
        user_nickname = dataDic['유저이름']
    else:
        user_nickname = None
    if '유저평가' in dataDic.keys():
        user_rate = dataDic['유저평가']
    else:
        user_rate = None
    if '남은시간' in dataDic.keys():
        user_left_time = dataDic['남은시간']
    else:
        user_left_time = None
    if '평가난이도' in dataDic.keys():
        user_difficulty = dataDic['평가난이도']
    else:
        user_difficulty = None
    if '탈출여부' in dataDic.keys():
        if dataDic['탈출여부'] == "실패":
            user_escape = False
        else:
            user_escape = True
    else:
        user_escape = None
    try:
        conn = pymysql.connect(host='localhost', user='root', password='dbtmdgns1345', port=3306, db='Escapable', charset='utf8')
        if not conn.open:
            print("연결 실패")
        with conn.cursor() as cursor:
            sql = "INSERT INTO review (cafe_name,thema_name, user_left_time, user_difficulty, user_escape, user_rate, user_nickname) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            #print(C_name,"   ", T_name,"   ", L_time,"   ", U_name,"   ", U_rate,"   ", R_time,"   ", U_diff)
            cursor.execute(sql, (cafe_name,thema_name, user_left_time, user_difficulty, user_escape, user_rate, user_nickname))
            conn.commit()
    finally:
        conn.close()

def insertDBthema(dataDic):
    if '카페이름' in dataDic.keys():
        cafe_name = dataDic['카페이름']
    else:
        cafe_name = None
    if '테마이름' in dataDic.keys():
        thema_name = dataDic['테마이름']
    else:
        thema_name = None
    if '제한시간' in dataDic.keys():
        thema_limit_time = dataDic['제한시간']
    else:
        thema_limit_time = None
    if '장르' in dataDic.keys():
        thema_genre = dataDic['장르']
    else:
        thema_genre = None
    if '난이도' in dataDic.keys():
        thema_level = dataDic['난이도']
    else:
        thema_level = None
    if '추천인원' in dataDic.keys():
        thema_number_of_people= dataDic['추천인원']
    else:
        thema_number_of_people = None
    if '테마정보' in dataDic.keys():
        thema_info= dataDic['테마정보']
    else:
        thema_info = None
    if '테마사진' in dataDic.keys():
        thema_picture= dataDic['테마사진']
    else:
        thema_picture = None
    try:
        conn = pymysql.connect(host='localhost', user='root', password='dbtmdgns1345', port=3306, db='Escapable', charset='utf8')
        if not conn.open:
            print("연결 실패")
        with conn.cursor() as cursor:
            sql = "INSERT INTO thema (cafe_name, thema_name, thema_limit_time, thema_genre, thema_level, thema_number_of_people, thema_info, thema_picture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            print(cafe_name,"   ", thema_name,"   ", thema_limit_time,"   ", thema_genre,"   ", thema_level,"   ", thema_number_of_people,"   ", thema_info,"  ",thema_picture)
            cursor.execute(sql, (cafe_name, thema_name, thema_limit_time, thema_genre, thema_level, thema_number_of_people, thema_info, thema_picture))
            conn.commit()
    finally:
        conn.close()

def insertDBcafe(dataDic):
    if '카페이름' in dataDic.keys():
        cafe_name = dataDic['카페이름']
    else:
        cafe_name = None
    if '카페정보' in dataDic.keys():
        cafe_info = dataDic['카페정보']
    else:
        cafe_info = None
    if '전화번호' in dataDic.keys():
        cafe_phone_number = dataDic['전화번호']
    else:
        cafe_phone_number = None
    if '카페주소' in dataDic.keys():
        cafe_address = dataDic['카페주소']
    else:
        cafe_address = None
    try:
        conn = pymysql.connect(host='localhost', user='root', password='dbtmdgns1345', port=3306, db='Escapable', charset='utf8')
        if not conn.open:
            print("연결 실패")
        with conn.cursor() as cursor:
            sql = "INSERT INTO cafe (cafe_name, cafe_info, cafe_number, cafe_address) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (cafe_name, cafe_info, cafe_phone_number, cafe_address))
            conn.commit()
    finally:
        conn.close()