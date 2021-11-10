# Parsing.py

from Connect import *
from bs4 import BeautifulSoup
class Parsing:
    def get_Cafe_Link(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        link = []
        for Page_div in soup.find_all('div',{"class":"m_ratio_inner"}):
            try:
                anchor = Page_div.find('a')
                href = anchor.get('href')
                if href.find('store') != -1:
                    if href not in link:
                        link.append(href)
            except AttributeError:
                continue
        return list(set(link))

    def get_Thema_Link(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        link = []
        for Page_div in soup.find_all('div',{"class":"theme_name"}):
            #print(Page_div)
            try:
                anchor = Page_div.find('a')
                href = anchor.get('href')
                #print(href)
                if href.find('theme') != -1:
                    if href not in link:
                        link.append(href)
            except AttributeError:
                continue
        return list(set(link))

    def parsing_Cafe(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        cafe_name = soup.find("div",{"class":"def_info_title"})
        cafe_name = cafe_name.find('span')
        cafe_info = soup.find("div",{"class":"desc"})
        cafe_info = cafe_info.find('span')
        phone_number = soup.find("div",{"class":"phone"})
        phone_number = phone_number.find("span",{"class":"text value"})
        cafe_address = soup.find("div",{"class":"address"})
        cafe_address = cafe_address.find("span",{"class":"text value"})
        info = dict()
        info["카페이름"] = cafe_name.get_text()
        info["카페정보"] = cafe_info.get_text()[0:300]
        info["전화번호"] = phone_number.get_text()
        info["카페주소"] = cafe_address.get_text()
        return info

    def parsing_Review(self):
        #print("파싱 시작")
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        #print("hello")
        # 맛집 이름
        info_list = []
        cafe = soup.find("div",{"class":"def_info_text_row def_info_theme_loc"})
        cafe = cafe.find('span')
        #print("카페이름  " + cafe.get_text())
        theme = soup.find("div",{"class":"def_info_text_row def_info_theme_name"})
        theme = theme.find('span')
        #print("테마이름  " + theme.get_text())
        limit_time = soup.find("div", {"class": "def_info_text_row def_info_theme_time"})
        limit_time = limit_time.find("span", {"class": "value"})
        #print("제한시간  " + time.get_text())
        Review_Item = soup.find_all("div",{"class" : "memb_review_box default"})
        for Review in Review_Item:
            info = dict()
            info['카페이름'] = cafe.get_text()
            info['테마이름'] = theme.get_text()
            #info['제한시간'] = time.get_text()
            if Review.find("span",{"class" : "name text"}) == None:
                continue
            if Review.find("div", {"class": "star"}).find("span", {"class": "text"}) == None:
                continue
            if Review.find("span", {"class": "level img"}) == None:
                continue
            if Review.find("span", {"class": "result_time text"}) == None:
                continue
            if Review.find("span", {"class": "experi img"}).find("span") == None:
                continue
            info['유저이름'] = Review.find("span",{"class" : "name text"}).get_text().strip('\n')
            info['유저평가'] = float(Review.find("div", {"class": "star"}).find("span", {"class": "text"}).get_text())
            images = Review.find("span", {"class": "level img"}).find('img')
            time_string = ""
            if Review.find("span", {"class": "result_time text"}).get_text() == '.':
                time_string = limit_time.get_text()
                if "분" not in time_string:
                    continue
                minute = int(time_string.split('분')[0])
                time = (minute*60)
                if images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_very_hard.png?ver=171754":
                    time *= -2
                elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_hard.png?ver=171754":
                    time *= -1
                elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_normal.png?ver=171754":
                    time *= -0.5
                elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_easy.png?ver=171754":
                    time *= -0.3
                elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_very_easy.png?ver=171754":
                    time = 0
                info['남은시간'] = int(time)
            else:
                time_string = Review.find("span", {"class": "result_time text"}).get_text()
            escape = Review.find("span", {"class": "experi img"}).find("span").get_text()
            info['탈출여부'] = Review.find("span", {"class": "experi img"}).find("span").get_text()
            if escape == "성공":
                if "분" not in time_string:
                    continue
                if "초" not in time_string:
                    continue
                #print(time_string)
                minute = int(time_string.split('분')[0])
                second = int(time_string.split('분')[1].split('초')[0])
                info['남은시간'] = minute*60 + second
            if images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_very_easy.png?ver=171754":
                info['평가난이도'] = 1
            elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_easy.png?ver=171754":
                info['평가난이도'] = 2
            elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_normal.png?ver=171754":
                info['평가난이도'] = 3
            elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_hard.png?ver=171754":
                info['평가난이도'] = 4
            elif images['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/review/difficulty_very_hard.png?ver=171754":
                info['평가난이도'] = 5
            #print(info)
            info_list.append(info)
        return info_list


    def parsing_Theme(self):
        # print("파싱 시작")
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        # print("hello")
        # 맛집 이름
        info_list = []
        cafe = soup.find("div", {"class": "def_info_text_row def_info_theme_loc"})
        cafe = cafe.find('span')
        # print("카페이름  " + cafe.get_text())
        theme = soup.find("div", {"class": "def_info_text_row def_info_theme_name"})
        theme = theme.find('span')
        # print("테마이름  " + theme.get_text())
        time = soup.find("div", {"class": "def_info_text_row def_info_theme_time"})
        time = time.find("span", {"class": "value"}).get_text()
        minute = int(time.split('분')[0])
        time = (minute * 60)
        # print("제한시간  " + time.get_text())
        genre = soup.find("div",{"class":"def_info_text_cell def_info_theme_genre_inner"})
        genre = genre.find("span",{"class":"value"})
        level = soup.find("div",{"class":"def_info_text_cell def_info_theme_difficulty"})
        level = level.find('img')
        if level['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/1_difficulty_white.png?ver=171754":
            level = 1
        elif level['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/2_difficulty_white.png?ver=171754":
            level = 2
        elif level['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/3_difficulty_white.png?ver=171754":
            level = 3
        elif level['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/4_difficulty_white.png?ver=171754":
            level = 4
        elif level['src'] == "https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/5_difficulty_white.png?ver=171754":
            level = 5
        activity = soup.find("div", {"class": "def_info_text_row def_info_theme_activity"})
        if activity.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/low_on.png"}):
            activity = 1
        elif activity.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/normal_on.png"}):
            activity = 2
        elif activity.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/many_on.png"}):
            activity = 3
        people_recommand = soup.find("div",{"class":"def_info_text_row def_info_theme_allow_user"})
        people_string = ""
        if people_recommand.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/2_user.jpg"}) != -1:
            people_string += "2인,"
        if people_recommand.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/3_user.jpg"}) != -1:
            people_string += "3인,"
        if people_recommand.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/4_user.jpg"}) != -1:
            people_string += "4인,"
        if people_recommand.find("img",{"src":"https://www.roomescape.co.kr/_template/assets/img/theme/detail/def_info/5_user.jpg"}) != -1:
            people_string += "5인 이상"
        thema_info = soup.find("div",{"class":"desc"})
        thema_info = thema_info.find("span")
        thema_pic = soup.find("div",{"class":"def_info_pic"})['style']
        thema_pic = thema_pic[21:-1]
        info = dict()
        info['카페이름'] = cafe.get_text()
        info['테마이름'] = theme.get_text()
        info['제한시간'] = time
        genre = genre.get_text()
        genre = genre.replace('\n',"")
        genre = genre.replace('\t',"")
        info['장르'] = genre
        info['난이도'] = level
        info['추천인원'] = people_string
        thema = thema_info.get_text()[0:300]
        info['활동성'] = activity
        info['테마정보'] = thema
        info['테마사진'] = thema_pic
        info_list.append(info)
        return info_list