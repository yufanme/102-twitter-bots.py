from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

service = Service(executable_path="/Users/fan/Development/chromedriver")
driver = webdriver.Chrome(service=service)

# driver.set_window_size(500, 400)
driver.get("https://crossbrowsertesting.github.io/selenium_example_page.html")

print(driver.page_source)