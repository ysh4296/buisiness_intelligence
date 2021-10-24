#ElementControl.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Connect import *
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#음식점 페이지의 리뷰를 확인
class Find_Review:
    def __init__(self, url):
        connect(url)

    # 더보기 버튼 클릭
    def more(self):
        while (1):
            try:
                tag = driver.find_element(By.XPATH, "//div[@class='RestaurantReviewList__MoreReviewButton']")
                action = ActionChains(driver)
                action.move_to_element(tag).perform()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "RestaurantReviewList__MoreReviewButton")))
                time.sleep(1)
                driver.find_element(By.XPATH, "//div[@class='RestaurantReviewList__MoreReviewButton']").click()
                print("click more")
            except ElementNotVisibleException:
                break
            except WebDriverException:
                break
            except AttributeError:
                break