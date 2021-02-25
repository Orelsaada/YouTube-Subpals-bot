from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import os
from tqdm import tqdm as prog

    

    
channel_id =    'YOUR YOUTUBE ID' #INSERT ID YOUTUBE
channel_pass =  'YOUR PASSWORD' #INSERT PASS YOUTUBE
my_email =      'YOUR EMAIL' # INSERT EMAIL GOOGLE
email_pass =    'YOUR EMAIL PASS' #INSERT PASSWORD EMAIL GOOGLE
user_data_dir = 'YOUR DIR CHROME PROFILE'#C:\\Users\\{YOUR USER}\\AppData\\Local\\Google\\{YOUR CHROME}\\User Data\\Default
not_show_chrome = False
delay_action = 6 #delay for action
delay_popup = 40 #delay for get stats
max_attempt = 10
attempt = 0
script_folder = os.path.dirname(__file__)
driver_folder = os.path.join(script_folder,'chromedriver.exe')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.OKGREEN}[==========================================================]{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}                   {bcolors.BOLD}BOT FOR SUBPALS  \n                 GET FLOW AND LIKE !{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}[==========================================================]{bcolors.ENDC}")

option = Options()


option.add_argument("--user-data-dir={}".format(user_data_dir))
option.add_argument('--profile-directory=Default')
option.add_argument("--use-fake-ui-for-media-stream")
option.add_argument("--disable-user-media-security=true")
option.headless = not_show_chrome
driver = webdriver.Chrome(driver_folder, options=option)
url_sub = 'https://www.subpals.com/pt/login/final/{}/'.format(channel_id)

# initialize process
driver.get(url=url_sub)
driver.implicitly_wait(10)
# storing the current window handle to get back to dashbord 
main_page = driver.current_window_handle 
driver.find_element(By.NAME, 'channelid').send_keys(channel_id)  # channel id
driver.find_element_by_name('password').send_keys(channel_pass)  # Channel password
driver.find_element_by_xpath("//button[@type='submit']").click()



print(f"{bcolors.OKGREEN}[+]Logged to SubPals.[+]{bcolors.ENDC}")

try:
    driver.find_element_by_xpath('//*[@class="userContent_pricing"]/div[2]/div[1]/div/div[2]/div[2]/form/a').click()  # activate plan
    print(f"{bcolors.OKGREEN}[+]Plan is already activated.{bcolors.ENDC}")
except:
    print(f"{bcolors.OKCYAN}[+]Plan is already activated.{bcolors.ENDC}")
    
time.sleep(delay_action)

#Get videos remain
try:
    left_videos = int(driver.find_element_by_id('remainingHint').text)
    print(f'{bcolors.OKBLUE}[+] {left_videos} videos [+]{bcolors.ENDC}')
#Except, for info last use in timestamp
except:
    time.sleep(20)
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="the-price__activated--countdown"]/div/iframe'))
    h_txt = driver.find_element_by_xpath('//*[@class="countdown-row countdown-show3"]/span[1]/span[1]').text
    mm_txt = driver.find_element_by_xpath('//*[@class="countdown-row countdown-show3"]/span[2]/span[1]').text
    print(f"{bcolors.WARNING}[==========================================================]{bcolors.ENDC}")
    print(f"{bcolors.WARNING}[-] You already used the program in the last {bcolors.BOLD} {h_txt} hours {mm_txt} min.{bcolors.ENDC}")
    print(f"{bcolors.WARNING}[==========================================================]{bcolors.ENDC}")
    driver.close()
    quit()
pbar = prog(total=left_videos)
driver.implicitly_wait(8)
#WORK LIKE AND FOLLOW YOUTUBE
while left_videos:
    driver.implicitly_wait(8)
    try:
        driver.find_element_by_xpath("//a[@id='likeSub2']").click()
        time.sleep(delay_action)
    except:
        print(f"{bcolors.FAIL}[-] Error when clicking the button{bcolors.ENDC}")
        driver.refresh()
        driver.implicitly_wait(10)
        print(f"{bcolors.WARNING}\n[.] Trying Another Alternative!{bcolors.ENDC}")
        while(attempt <= max_attempt):
            attempt +=1
            driver.refresh()
            driver.implicitly_wait(8 + attempt)
            try:
                driver.find_element_by_xpath("//div[@id='likeSub2']/a").click()
                break
            except:
                print(f"{bcolors.FAIL}[-]{str(attempt)}x Error when clicking the button {bcolors.ENDC}")
            if(attempt == max_attempt):
                print(f"{bcolors.FAIL}[-] Maximum attempts exceeded {bcolors.ENDC}")
                pbar.close()
                driver.close()
                quit()
    attempt=0
    #VERIFY POPUP
    for handle in driver.window_handles: 
        if handle != main_page: 
            yt_page = handle 
    #INTO POPUP
    driver.implicitly_wait(2)
    try:
        driver.switch_to.window(yt_page)
        print(f"{bcolors.OKGREEN}[.] Changing Page{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}[-] Popup not found{bcolors.ENDC}")
        time.sleep(delay_action)
        driver.close()
        pbar.close()
        quit()
    #LOGIN YOUTUBE   
    driver.implicitly_wait(4) 
    try:
        driver.find_element_by_xpath('//*[@class="style-scope ytd-masthead style-suggestive size-small"]/a').click()
        driver.find_element_by_id('identifierId').send_keys(my_email)
        driver.find_element_by_id('identifierNext').click()
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(email_pass)
        password_input.send_keys(Keys.RETURN)
    except:
        print(f"{bcolors.OKGREEN}[+] Logged to Youtube. [+]{bcolors.ENDC}")
    print(f"{bcolors.WARNING}[.] Continuing{bcolors.ENDC}")
    # Like and Sub:
    driver.implicitly_wait(delay_action)
    print(f"{bcolors.OKCYAN}[.] Enjoying{bcolors.ENDC}")
    like_button = driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
    time.sleep(delay_action)
    print(f"{bcolors.OKCYAN}[.] Following{bcolors.ENDC}")
    sub_button = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()
    time.sleep(delay_action)
    driver.implicitly_wait(2)
    print(f"{bcolors.OKCYAN}[.] Changing Page{bcolors.ENDC}")
    driver.switch_to.window(main_page)
    driver.implicitly_wait(4)
    print(f"{bcolors.WARNING}[.] Clicking continue ... Wait!{bcolors.ENDC}")
    try:
        driver.find_element_by_xpath('//*[@id="likeSub3"]/a').click()
    except:
        print(f"{bcolors.FAIL}[-] Trying Another Alternative!{bcolors.ENDC}")
        driver.refresh()
        driver.implicitly_wait(5)
        print(f"{bcolors.WARNING}\n[.] Trying Another Alternative!{bcolors.ENDC}")
        while(attempt <= max_attempt):
            attempt +=1
            driver.refresh()
            driver.implicitly_wait(8 + attempt)
            try:
                driver.find_element_by_xpath('//*[@id="likeSub3"]/a').click()
                break
            except:
                print(f"{bcolors.FAIL}[-] {str(attempt)}x Error when clicking the continue button {bcolors.ENDC}")
            if(attempt == max_attempt):
                print(f"{bcolors.FAIL}[-] Maximum attempts exceeded{bcolors.ENDC}")
                pbar.close()
                driver.close()
                quit()
    attempt=0
    time.sleep(40)   
    try:
        left_videos = int(driver.find_element_by_id('remainingHint').text)
        print(f"{bcolors.OKBLUE}[+] {left_videos} videos [+]{bcolors.ENDC}")
        print("[.] Continuing cycle[.]")
    except:
        print("[==========================================================]")
        print(" No more videos left on SubPals.")
        print("[==========================================================]")
        pbar.update(1)
        time.sleep(60)
        driver.close()
        pbar.close()
        quit()
    pbar.update(1)
    time.sleep(delay_action)
#END WORK
print(f"{bcolors.OKGREEN}[==========================================================]{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}[*] {bcolors.BOLD}!!!!Finish Bot, congratulation!!!!!{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}[==========================================================]{bcolors.ENDC}")
time.sleep(60)
driver.close()
pbar.close()
quit()
