""" Result with Google """
import webbrowser as web


"""  RESULT ON WEB BROWSER  """

# Search query on Google engine
def google_ask(topic):
    try:
      web.open(f"https://www.google.com/search?q={topic}")
    except Exception as e:
        print("check your internet", e)

# open web on browser
def website(name):
    try:
        url = f"https://www.{name}.com"
        web.open(url)
    except Exception as e:
        print("check your internet", e)

# Search query on youtube
def play_yt(topic: str, open_video: bool = True):
    try:
        url = f"https://www.youtube.com/results?q={topic}"
        web.open(url)
    except Exception as e:
        print("check your internet", e)


# test functions
if __name__ == "__main__":
    google_ask("cs50p")
    play_yt("bharat")
    website("instagram")