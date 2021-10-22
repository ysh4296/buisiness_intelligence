#Main.py
# using utf-8

from Connect import *
from ElementControl import *
from Parsing import *
from DBConnect import *

if __name__ == "__main__":
    #해쉬태그를 수집하여 저장
    collect = []


    # 웹 활용 객체
    driver = Toplist()
    # 웹 파싱 객체
    p = Parsing()

    #해쉬태그 수집
    hashTag = driver.collectHashTag()

    #해쉬태그 클릭 후 URL 수집
    for i in hashTag:
        driver.tagClick(i)
        driver.more()
        collect.append(p.getLink())