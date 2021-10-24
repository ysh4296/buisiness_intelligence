# Parsing.py

from Connect import *
from bs4 import BeautifulSoup
class Parsing:
    # 음식점 URL 수집
    def get_Rest_Link(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        link = []
        for Page_Button in soup.find_all('a',{"class":"only-desktop_not"}):
            try:
                if Page_Button.get('href').find('restaurants') != -1:
                    if Page_Button.get('href').find('restaurant_key') == -1:
                        if Page_Button.get('href') not in link:
                            link.append(Page_Button.get('href'))
                            print(str(Page_Button.get('href')))
            except AttributeError:
                continue
        return list(set(link))

    def parsing_Review(self):
        print("파싱 시작")
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
            # 맛집 이름
            info_list = []
            title = soup.find("h1",{"class":"restaurant_name"})
            print("음식점 이름  " + title.get_text())
            Review_Item = soup.find_all("a",{"class" : "RestaurantReviewItem__Link"})
            for Review in Review_Item:
                info = dict()
                info['음식점이름'] = title.get_text()
                info['유저이름'] = Review.find("span",{"class" : "RestaurantReviewItem__UserNickName"}).get_text()
                info['유저평가'] = Review.find("span",{"class" : "RestaurantReviewItem__RatingText"}).get_text()
                print(Review.find("span", {"class": "RestaurantReviewItem__UserNickName"}).get_text(), "  ",
                      Review.find("span", {"class": "RestaurantReviewItem__RatingText"}).get_text())
                info_list.append(info)
            return info_list
        except AttributeError:
            print("없음")