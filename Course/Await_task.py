from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import sin, log
import time

link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    options = Options()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(link)
    
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    res = log(abs(12*sin(int(x))))
    browser.find_element(By.ID, 'answer').send_keys(str(res))
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(30)
    browser.quit()
