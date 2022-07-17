from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import os


# todo 1 login
# todo 2 click follow
# todo 3 close

SCROLL_DOWN_TIMES = 300


class TwitterBot:
    def __init__(self):
        self.DRIVER_PATH = "/Users/fan/Development/chromedriver"
        self.EMAIL = os.environ.get("EMAIL")
        self.PASSWORD = os.environ.get("PASSWORD")
        self.service = Service(executable_path=self.DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login_twitter(self):
        print("begin login.")
        self.driver.get("https://twitter.com/")
        sign_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_button.click()
        # input email
        email_input_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "text")))
        email_input_box.send_keys(self.EMAIL)
        time.sleep(random.random() * 3)
        email_input_box.send_keys(Keys.ENTER)
        password_inpu_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
        password_inpu_box.send_keys(self.PASSWORD)
        time.sleep(random.random() * 3)
        password_inpu_box.send_keys(Keys.ENTER)
        print("login success.")
        # wait for new page
        time.sleep(3)
        self.driver.get("https://twitter.com/xiaolai/following")


    def click_follow(self):
        time.sleep(5)
        followed = 0
        count = 0
        round_times = 0
        for _ in range(SCROLL_DOWN_TIMES):
            round_times += 1
            # print("scroll down page.")
            body = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body")))
            body.send_keys(Keys.END)

            if round_times < 165:
                print(f"round is {round_times}.")
                time.sleep(3)
                continue
            else:
                # ElementClickInterceptedException. often happen.
                time.sleep(8)
            if round_times == SCROLL_DOWN_TIMES:
                self.driver.quit()

            for order in range(1, 55):
                count += 1
                try:
                    current_element = WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > section > div > div > div:nth-child({order}) > div > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-19u6a5r > div > div > span > span")))
                    # current_element = self.driver.find_element(By.CSS_SELECTOR, f"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > section > div > div > div:nth-child({order}) > div > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-19u6a5r > div > div > span > span")
                    print(f"{current_element.text}, count is: {count}, already followed {followed}.")
                    if current_element.text == "关注":
                        time.sleep(2)
                        current_element.click()
                        print(f"{_} round, order {order} have clicked follow.")
                        followed += 1
                        # sleep 300 seconds every follow 50 people.
                        if followed != 0 and followed % 30 == 0:
                            print("sleeping for 300 seconds.")
                            time.sleep(300)
                        # sleep 2~4 seconds after click follow.
                        time.sleep(random.uniform(2, 4))
                except TimeoutException:
                    print("TimeoutException.")
                    continue
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    continue
                except ElementClickInterceptedException:
                    print("ElementClickInterceptedException.")
                    continue