# Import required libraries
import os
import webbrowser
import pyautogui
from time import sleep
import speech_recognition as sr
import re

# My packages
from browser import play_yt, google_ask, website  # To use websites on browser
from open_ai import openai_ask  # To use open AI chatGPT
from spotify_web import direct_play, login, search_play, lab_sch_play, like_plist, current_play, like_song, forward_song, backward_song, home # To use spotify web music
from tools import say, wish, save_result, take_ss  # To take screenshot, save file, etc...


# Audio into text function...
def get_audio():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio= r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in").lower()  # return result text in lowercase
            print(f"User said🔊 {query}")
            return query
    except Exception:
        return "something went wrong"


"""   ALL VIRTUAL ASSISTANT COMMANDS   """

def main():
    # wish to time
    say(wish())
    say("i am  your virtual assistant sir, please tell me how may i help you")

    # Listening continuously...
    while True:
        print("Listening...")
        query = get_audio()  # All text outputs  in lowercase
        web_browser(query)
        my_computer(query)
        spotify_music(query)
        openai_gpt(query)


# todo: Website on webbrowser commands
def web_browser(query):

    # Open direct logged in websites
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["python status", "https://cs50.me/cs50p"],
        ["facebook", "https://www.facebook.com"],
        ["instagram", "https://www.instagram.com"],
        ["linkedin", "https://www.linkedin.com"],
        ["github", "https://www.github.com"],
        ["telegram", "https://web.telegram.org/k/"],
        ["stack overflow", "https://stackoverflow.com/"],
        ["canva", "https://canva.com/"],
    ]
    for site in sites:
        if f"open {site[0]}" in query:
            say(f"opening {site[0]}")
            webbrowser.open(site[1])

       # Open new or non logged in websites
        elif "website" in query:
            web = query.removeprefix("open ").replace(" website", "").removesuffix(" open")
            website(web)
            break

    # search on google
    if "on google" in query:
        ask = query.replace(" on google", "")
        google_ask(ask)
        sleep(3)
        say("these are google result")

    # search on youtube
    elif "on youtube" in query:
        video = query.replace("on youtube", "")
        play_yt(video)
        sleep(3)
        say("these are videos on searched topic")

    # close current website in browser
    elif "close webpage" in query or "close website" in query or "close this website" in query or "close current website" in query or "close current webpage" in query:
        pyautogui.hotkey("ctrl", "w")
        say("sure")


# todo: My computer commands
def my_computer(query):

    # open application cmd
    apps = [
    ["vlc", r"C:\Users\Public\Desktop\VLC media player.lnk"],
    ["chrome", r"C:\Users\Public\Desktop\Google Chrome.lnk"],
    ]
    for app in apps:
        if f"open {app[0]}" in query or f"open {app[0]} app" in query or f"open {app[0]} application" in query:
            say(f"opening {app[0]} application")
            os.system(app[1])

    # close applications cmd
    apps = [
    ["vlc", r"taskkill /im vlc.exe"],
    ["chrome", r"taskkill /im chrome.exe"]
    ]
    for app in apps:
        if f"close {app[0]}" in query or f"exit {app[0]}" in query or f"close {app[0]} app" in query or f"close {app[0]} application" in query:
            os.system(app[1])
            say(f"{app[0]} is closed")

    # Take screenshot cmd
    if "take screenshot" in query or "take a screenshot" in query:
        take_ss("ai_shot")  # screenshot save in tools file !!
        print("Your Screenshot is save in tools package file !!")
        say("got it")

    # For exit program
    elif "close program" in query or "exit program" in query:
        say("program is closing, have a good day master")
        exit()

    # open history file command
    elif "chat history file" in query or "history file" in query:
        os.system("chat_history.txt")


# todo: sportify  music cmds
def spotify_music(query):

    # direct search song/playlist and play
    if "on spotify" in query:
        songs = re.search(r'\b\s*(.*?)\s*\bon\s*spotify\b', query).group(1).replace("play","").replace("search", "")
        direct_play(songs)
        sleep(2)
        say("searched song is playing")


    # spotify web commands...
    elif "open spotify" in query or "music app" in query:
        try:
            say("opening spotify")
            login()
            say("spotify is opened, what would you like to listen")
        except Exception:
            say("i think somthing went wrong, please check your internet and chrome browser permission ")

    elif "search song" in query or "search playlist" in query:
        song = query.replace("search","").replace("song", "")
        search_play(song)
        sleep(2)
        say("searched song is playing")

    elif "play song" in query or "stop song" in query:
        current_play()
        say("okay")

    elif "like song" in query or "like this song" in query or "unlike song" in query or "unlike this song" in query:
        like_song()
        say("done")

    elif "like playlist" in query or "like this" in query or "unlike playlist" in query or "unlike this playlist" in query:
        like_plist()
        say("done")

    elif "search in library" in query or "in library" in query:
        plist = query.replace("search in library", "").replace("in library", "")
        lab_sch_play(plist)
        sleep(2)
        say("searched playlist is playing")

    elif "back to home"  in query or "go to home" in query or "open home page" in query:
        try:
            home()
            say("allright")
        except Exception:
            print("That's spotify_web command")

    elif "change song" in query or "next song" in query:
        try:
            forward_song()
        except Exception:
            say("spotify is not open")

    elif "play again" in query or "back song" in query or "play past song" in query:
        try:
            backward_song()
        except Exception:
            say("spotify is not open")


# todo: open AI cmds
def openai_gpt(query):

    # result from open_ai 'chat gpt'
    if "explain" in query or "in detail" in query or "open ai" in query or "gpt" in query or "essay" in query or "application" in query or "letter" in query:
        result = openai_ask(query=query)

        # say or read only 1 or 2 sentences
        sentences = re.findall(r'[^.!?]*[.!?]', result)
        [say(sentence.strip()) for sentence in sentences[:1]]

        # save detail answer in file
        print(result, "\n\nThis result is also save in chat_history.txt file")
        save_result(result)
        say("The detail answer is also save in chat history.txt file")

    # if wh or how in query so return that's answer
    elif re.search(r'\bwh\w+\b|how\b', " ".join(query.split()[:5]), re.IGNORECASE):
        result = openai_ask(query=f"{query} give short answer")
        print(result)
        say(result)


# Call main function to run program
if __name__ == "__main__":
    main()