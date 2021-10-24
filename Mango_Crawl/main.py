#Main.py
# using utf-8

from DBConnect import *
from ElementControl import *
from Parsing import *

if __name__ == "__main__":
    p = Parsing()
    List = []
    for i in range(1,11):
        url = "search/서울?keyword=서울&page=" + i.__str__()
        connect(url)
        print(i.__str__() + "  page")
        List = p.get_Rest_Link()
        for URL in List:
            Review_Crawl = Find_Review(URL)
            Review_Crawl.more()
            try:
                info_list = (p.parsing_Review())
                print("num of review")
                for info in info_list:
                    print(type(info))
                    insertDB(info)
            except:
                continue
