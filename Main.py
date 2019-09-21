from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions


channel_id = input('Enter your channel id: ')
channel_pass = input('Enter your channel password: ')
my_email = input('Enter your email: ')
email_pass = input('Enter your email password: ')


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("F:\Python\Projects\ChromeWebdriver\chromedriver.exe",options=chrome_options)

driver.get(url="https://www.subpals.com/")
driver.implicitly_wait(10)


login_register = driver.find_element(By.XPATH,'//*[@id="mega-menu-item-32613"]/a')
driver.execute_script("arguments[0].click();", login_register)


driver.switch_to.frame(1)

driver.find_element(By.NAME, 'channelid').send_keys(channel_id)  # channel id

login_button = driver.find_element(By.NAME, 'submit')
driver.execute_script("arguments[0].click();", login_button)

driver.find_element_by_name('password').send_keys(channel_pass)  # Channel password

login_button = driver.find_element(By.NAME, 'submit')
driver.execute_script("arguments[0].click();", login_button)     # LOGIN SUBPALS

driver.refresh()

driver.switch_to.frame('iFrameResizer0')
try:
    driver.find_element_by_xpath('/html/body/div/center[2]/div/div[1]/div[2]/form/div/a').click() #activate plan
except:
    pass
time.sleep(5)
try:
    left_videos = int(driver.find_element_by_id('remainingHint').text)
    print(f'[+] {left_videos} videos [+]')

    while left_videos:
        try:
            driver.switch_to.frame("iFrameResizer0")
        except:
            pass
        first_button = driver.find_element_by_id('likeSub2')
        driver.execute_script("arguments[0].click();", first_button)
        driver.switch_to.window(driver.window_handles[1])

        try:
            # Login to Youtube:
            youtube_login = driver.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/a')
            driver.execute_script("arguments[0].click();", youtube_login)
            driver.find_element_by_id('Email').send_keys(my_email)
            next_button = driver.find_element(By.ID, 'next')
            driver.execute_script("arguments[0].click();", next_button)

            driver.find_element(By.ID, 'Passwd').send_keys(email_pass)
            pass_next_button = driver.find_element(By.ID, 'signIn')
            driver.execute_script("arguments[0].click();", pass_next_button)
            print("Logined to youtube")
        except:
            pass

        # Like and Sub:
        like_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
        sub_button = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.frame("iFrameResizer0")
        time.sleep(7)

        confirm_button = driver.find_element_by_id('likeSub3')
        driver.execute_script("arguments[0].click();", confirm_button)

        WebDriverWait(driver, 50).until(
            ec.invisibility_of_element_located((By.ID, 'likeSub3')))
        try:
            left_videos = int(driver.find_element_by_id('remainingHint').text)
            print(f'[+] {left_videos} videos [+]')
        except:
            print("No more videos left on SubPals.")
            break
        time.sleep(2)

except exceptions.NoSuchElementException:
    print("You already used it in the last 24 hours.")
