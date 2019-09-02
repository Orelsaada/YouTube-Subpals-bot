from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome("F:\chromedriver.exe")

driver.get(url="https://www.subpals.com")
driver.implicitly_wait(10)

 #Canceling the ad
time.sleep(10)
driver.find_element(By.ID,'image-f2c4f9b9f6bd33e7629a866a5dbb5955').click() 

driver.find_element(By.LINK_TEXT,'Login / Register').click()

driver.switch_to.frame(1)

#channel id
driver.find_element(By.NAME, 'channelid').send_keys('ENTER HERE YOUR CHANNEL ID')    <---- Enter Channel ID.

login_button = driver.find_element(By.NAME, 'submit')
driver.execute_script("arguments[0].click();", login_button)

#Channel password
driver.find_element_by_name('password').send_keys('ENTER HERE YOUR CHANNEL PASSWORD')   <---- Enter your channel password

#Logging to SubPals
login_button = driver.find_element(By.NAME, 'submit')
driver.execute_script("arguments[0].click();", login_button)     

driver.switch_to.frame('iFrameResizer0')

#Activate the plan
try:
    driver.find_element_by_xpath('/html/body/div/center[2]/div/div[1]/div[2]/form/div/a').click() 
except:
    pass
time.sleep(5)

#20 times of likes and sub
for i in range(21):
    if i == 0:
        try:
            driver.switch_to.frame("iFrameResizer0")
        except:
            pass

        driver.find_element_by_id('likeSub2').click()

        driver.switch_to.window(driver.window_handles[1])

        #Login to Youtube:
        driver.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/a').click()

        driver.find_element(By.ID, 'identifierId').send_keys('ENTER HERE YOUR EMAIL') <---- Enter here your email
        driver.find_element(By.ID, 'identifierNext').click()

        driver.find_element(By.NAME, 'password').send_keys('ENTER HERE YOUR EMAIL PASSWORD') <---- Enter here your email password
        pass_next_button = driver.find_element(By.ID, 'passwordNext')
        driver.execute_script("arguments[0].click();", pass_next_button)

        #Like and Sub:
        like_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
        sub_button = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()

        driver.switch_to.window(driver.window_handles[0])

        driver.switch_to.frame("iFrameResizer0")
        time.sleep(7)
        driver.find_element_by_id('likeSub3').click()
        time.sleep(5)

    else:
        driver.refresh()
        time.sleep(5)
        driver.switch_to.frame("iFrameResizer0")
        driver.find_element_by_id('likeSub2').click()

        driver.switch_to.window(driver.window_handles[1])

        # Like and Sub:
        like_button = driver.find_element_by_xpath(
            '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
        sub_button = driver.find_element_by_xpath(
            '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()

        driver.switch_to.window(driver.window_handles[0])

        time.sleep(10)

        driver.switch_to.frame("iFrameResizer0")
        driver.find_element_by_id('likeSub3').click()
        time.sleep(6)

