#ElementControl.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Connect import *
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains


class Find_Cafe:#테마 및 리뷰 크롤링
    def __init__(self):
        initpage()
    # 더보기 버튼 클릭
    def more(self):
        while (1):
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "theme_list_more_btn")))
                tag = driver.find_element(By.XPATH, "//button[@id='theme_list_more_btn']")
                action = ActionChains(driver)
                action.move_to_element(tag).perform()
                tag.click()
                #driver.find_element(By.XPATH, "//button[@id='theme_list_more_btn']").click()
                #print("click more")
            except ElementNotVisibleException:
                break
            except WebDriverException:
                break
            except AttributeError:
                break
    def click_loc(self):
        try:
            loc = driver.find_element(By.XPATH, "//div[@id='loc_category_reveal']")
            loc.click()
            action = ActionChains(driver)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='loc_select_btn select_inner select_2_inner']")))# 홍대
            tag = driver.find_element(By.XPATH, "//span[@class='loc_select_btn select_inner select_2_inner']")  # 홍대

            action.move_to_element(tag).perform()
            tag.click()
            loc.click()
            search = driver.find_element(By.XPATH, "//button[@id='search_btn']")# 검색
            action.move_to_element(search).perform()
            search.click()
        except AttributeError:
            return

class Find:#카페크롤링
    def __init__(self):
        initpage()
    # 더보기 버튼 클릭
    def more(self):
        while (1):
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "company_list_more_btn")))
                tag = driver.find_element(By.XPATH, "//button[@id='company_list_more_btn']")
                action = ActionChains(driver)
                action.move_to_element(tag).perform()
                tag.click()
            except ElementNotVisibleException:
                break
            except WebDriverException:
                break
            except AttributeError:
                break
    def click_loc(self):
        try:
            loc = driver.find_element(By.XPATH, "//div[@id='loc_reveal']")
            loc.click()
            action = ActionChains(driver)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@data-loc='홍대']")))
            tag = driver.find_element(By.XPATH, "//span[@data-loc='홍대']")  # 홍대

            action.move_to_element(tag).perform()
            tag.click()
            loc.click()
            search = driver.find_element(By.XPATH, "//button[@id='search_btn']")# 검색
            action.move_to_element(search).perform()
            search.click()
        except AttributeError:
            return