""" There are some small tool 'function' in this file """
import pyttsx3
import datetime
from PIL import ImageGrab
import time


"""   SOME OFFLINE TOOL FOR VIRTUAL ASSISTANT"""

# -----Voices index in my pc
# (voices[0])#David
# (voices[1])#James
# (voices[2])#Linda
# (voices[3])#Richard
# (voices[4])#George
# (voices[5])#Hazel
# (voices[6])#Susan
# (voices[7])#Sean
# (voices[8])#Heera
# (voices[9])#Ravi
# (voices[10])#David
# (voices[11])#Mark
# (voices[12])#Zira
# (voices[13])#Hemant
# (voices[14])#Kalpana
# (voices[15])#Hazel
# (voices[16])#Catherine
# (voices[17])#Zira

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
rate = engine.getProperty('rate')  # getting details of current speaking rate

# Text to speech  function
def say(text):
    try:
        engine.setProperty('voice', voices[16].id)  # changing index, changes voices.
        engine.setProperty('rate', 185)     # setting up new voice rate
        engine.say(text)
        engine.runAndWait()
    except Exception:
        # default tts voice in windows
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()

# wish with time function
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return "good morning"
    elif hour >= 12 and hour < 18:
        return "good afternoon"
    else:
        return "good evening"


# Take Screenshot of the Screen function
def take_ss(file_name: str = "AI_screenshot", delay: int = 1, show: bool = True) -> None:
    try:
        time.sleep(delay)
        screen = ImageGrab.grab()
        if show:
            screen.show(title=file_name)
        screen.save(f"{file_name}.png")
    except Exception as e:
        print("somthing went wrong", e)


# Function to save history of chats
def save_result(result):
    try:
        # if not os.path.exists("openai_history.txt"):
        result = result.encode('ascii', 'ignore').decode('ascii')
        with open("chat_history.txt", "a") as file:
            file.write(f">-->\n{result}\n<--<\n\n")
    except Exception as e:
        print("somthing went wrong", e)


# -----test the program
if __name__ == "__main__":
    say(wish())
    say("hello sir This is my c s 50 final project part and this is text to speech program")
    take_ss("ai shot")

