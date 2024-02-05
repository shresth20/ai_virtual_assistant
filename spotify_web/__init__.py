#All requried packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import webbrowser


# module and element to control chrome browser
options = webdriver.ChromeOptions()
options.headless = False  # false for run
options.add_experimental_option("detach", True)
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
service = Service()
driver = webdriver.Chrome(options=options, service=service)



"""     FUNCTIONS  TO  CONTROLE SPOTIFY WEB        """


# Info for spotify web to login
def spotify_id_pass():
    try:
       Email, Password = "USERNAME", "PASSWORD"  # Email/ID, Password
       return Email, Password
    except Exception:
        print("Please enter your spotify id password in  ' project/spotify_web/__init__.py '  to auto login in  ")


#direct search play song/playlist
def direct_play(song: str) -> None:
        try:
            webbrowser.open(f"http://open.spotify.com/search/{song}")
            sleep(2)
            pyautogui.moveTo(x=583, y=420)  # drop pointer
            sleep(5)
            pyautogui.click(pyautogui.moveTo(pyautogui.locateOnScreen("playbutton.png", confidence=0.7)))
        except Exception as e:

            print("Make sure 'Browser window is Full Opened'", e)

# auto login fun..
def login():
    Email, Password = spotify_id_pass()

    # open login url page
    url = 'https://accounts.spotify.com/en/login'
    try:
        driver.get(url) 
        driver.maximize_window()
    except Exception:
        pass
    # WITH XPATH

    # login page
    try:
        driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys(Email)       # id box
        driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(Password)    # password box
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]/span[1]'))).click() # login button
    except Exception:
        pass
    # welcom page
    try:
        sleep(5)
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/button[2]/span[2]'))).click()  # web app button
        sleep(8)
    except Exception:
        pass
    # policy notice click cut...
    try:
        cut_button = driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        chain = ActionChains(driver)
        chain.move_to_element(cut_button).click().perform()
        sleep(5)
    except Exception:
        pass


# current song play button fun..
def current_play():
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/button'))).click()
    except Exception:
        pass


# current song like fun..
def like_song():
    try:
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[1]/div/button').click()
    except Exception:
        pass


# forward  song fun..
def forward_song():
    try:
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[2]/button[1]').click()
    except Exception:
        pass


# backward song fun..
def backward_song():
    try:
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[1]/button[2]').click()
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[1]/button[2]').click()
    except Exception:
        pass


# search song/playlist and play fun..
def search_play(text):
    try:
        driver.maximize_window()  # want full window to play properly
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[1]/ul/li[2]/a').click()    # search button
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input').send_keys(text)   # search box
        pyautogui.moveTo(x=583, y=420)  # drop pointer
        sleep(2)
        # click popup play button
        driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[3]/div/button').click()
    except Exception :
        pass


# enter text in search box fun..
def lab_sch_play(text):
    while True :
        try:
            # search input
            driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]').click()
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/input'))).send_keys(text)
            sleep(5)
            # first row click
            driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div[1]/div[2]/div[4]/div/div/div/div[2]/ul/div/div[2]/li[1]').click()
            sleep(4)
            # play button click
            driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/div/button').click()
            break
        except Exception as e:
            driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div[1]/div[1]/header/div/div/button').click()  # click lab icon


# like playlist in labirary fun..
def like_plist():
    try:
        driver.find_element(By.XPATH,
                            '//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[4]/div/div/div/div/button[1]').click()
    except Exception as e:
        print(e)
        pass


# home or back fun.
def home():
    try:
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/nav/div[1]/ul/li[1]/a').click()
    except Exception:
        pass



# test functions...
if __name__ == "__main__":
   # direct_play("mahakal ki gulami")
    login()
   #  sleep(2)
   #  search_play("jagarnath astakam")


    # sleep(30)
    # lab_sch_play("eng.song")
    #
    # sleep(10)
    # home()
    # sleep(30)
    # current_play()  # for stop
    #
    # sleep(30)
    # current_play() # for play
    #
    # sleep(30)
    # forward_song()
    #
    # sleep(30)
    # backward_song()
    #
    # sleep(30)
    # like_song()







