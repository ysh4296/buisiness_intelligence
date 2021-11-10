#Main.py
# using utf-8

from DBConnect import *
from ElementControl import *
from Parsing import *


if __name__ == "__main__":
    p = Parsing()
    List = []
    # Crawling cafe
    """
    Crawler = Find()
    Crawler.click_loc()
    Crawler.more()
    List = p.get_Cafe_Link()
    print(List)
    for url in List:
        connect(url)
        info = p.parsing_Cafe()
        insertDBcafe(info)
    """
    # Crawling thema
    """
    p = Parsing()
    List = []
    Crawler = Find_Cafe()
    Crawler.click_loc()
    Crawler.more()
    List = p.get_Thema_Link()
    #print(List)
    for url in List:
        print(url)
        connect(url)
        info_list = p.parsing_Theme()
        try:
            for info in info_list:
                insertDBthema(info)
        except:
            continue
    """
    # Crawling review
    """
   for url in List:
       connect(url)
       info_list = p.parsing_Review()
       try:
           for info in info_list:
               insertDBreview(info)
       except:
           continue
    """
