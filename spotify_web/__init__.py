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
options.headless = False  # false for run program
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
       Email, Password = " ", " "  # Email/ID, Password
       return Email, Password
    except Exception:
        print("Please enter your spotify id password in  'spotify_web/__init__.py '  to auto login in spotify_id_pass() function")
        return "Enter your Id Password in spotify_web/_init_.py in spotify_id_pass() function"


#direct search play song/playlist
def direct_play(song: str) -> None:
        try:
            webbrowser.open(f"http://open.spotify.com/search/{song}")
            sleep(2)
            pyautogui.moveTo(x=700, y=420)  # drop pointer
            sleep(7)
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
    except Exception as e:
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
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/footer[1]/div[1]/div[2]/div[1]/div[1]/button[1]'))).click()
    except Exception as e:
        print(e)
        pass


# current song like fun..
def like_song():
    try:
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/footer[1]/div[1]/div[1]/div[1]/button[1]').click()
    except Exception as e:
        print(e)
        pass


# forward  song fun..
def forward_song():
    try:
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/footer[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]').click()
    except Exception:
        pass


# backward song fun..
def backward_song():
    try:
        # Perform double click
        with ActionChains(driver) as actions:
            actions.double_click(driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/footer[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]')).perform()
    except Exception:
        pass


# search song/playlist and play fun..
def search_play(text):
    try:
        driver.maximize_window()  # want full window to play properly
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[2]').click() # search button
        try:
                driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[2]/div[3]/header[1]/div[3]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]/*[name()='path'][1]").click() # clear searched
        except Exception:
            pass
        sleep(1)
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[3]/header[1]/div[3]/div[1]/div[1]/form[1]/input[1]').send_keys(text)   # search box
        pyautogui.moveTo(x=583, y=470)  # drop pointer
        sleep(3)
        # click popup play button
        try:
            driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]/span[1]/*[name()='svg'][1]/*[name()='path'][1]").click()
        except Exception :
            pyautogui.moveTo(x=580, y=471)
            driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]/span[1]/*[name()='svg'][1]/*[name()='path'][1]").click()

    except Exception as e:
        print(e)
        pass



# enter text in search box fun..
def lab_sch_play(text):
    while True :
        try:
            # search input
            try:
                driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]').click()
            except Exception :
                driver.find_element(By.XPATH," /html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1] ").click() # cut buttoon then input

            try:
                driver.find_element(By.XPATH," /html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1] ").click() # cut buttoon then input
            except Exception:
                pass
            # input text
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'))).send_keys(text)
            sleep(5)
            # first row click
            driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/ul[1]/div[1]/div[2]/li[1]/div[1]/div[1]').click()
            sleep(4)
            # play button click
            driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]').click()
            break
        except Exception as e:
            driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/button[1]').click()  # click lab icon
        except Exception:
            pass

# like playlist in labirary fun..
def like_plist():
    try:
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]/*[name()='path'][1] ").click()
    except Exception as e:
        print(e)
        pass


# home or back fun.
def home():
    try:
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[1]/nav[1]/div[1]/ul[1]/li[1]').click()
    except Exception:
        pass



# test functions...
if __name__ == "__main__":
   direct_play("mahakal ki gulami")
    # login()
    # #
    # sleep(2)
    # search_play("jagarnath astakam")
    #
    # sleep(12)
    # search_play("panjabi")
     #
    # sleep(15)
    # lab_sch_play("this is kaka")
    #
    # sleep(15)
    # lab_sch_play("this is serhat")
    #
    # sleep(30)
    # home()
    #
    # sleep(5)
    # current_play()  # for stop
    #
    # sleep(30)
    # current_play() # for play
    #
    # sleep(5)
    # forward_song()
    #
    # sleep(10)
    # backward_song()
    #
    # sleep(10)
    # backward_song()
    #
    # sleep(5)
    # like_song()
   #
    # sleep(5)
    # like_plist()








