"""  TEST  FILE  TO  TEST  PROJECT  """

# NOTE : Please fill openai api key in 'project/open_ai/__init__.py' package and sportify id password in 'project/spotify_web/__init__.py' then run the test program nother you get some error !!

import pytest
from project import web_browser,spotify_music, openai_gpt

def main():
    test_web_browser_open_python_status()
    test_web_browser_open_facebook()
    test_spotify_music_open_spotify()
    test_spotify_music_search_song()
    test_openai_gpt_in_detail()
    test_openai_gpt_short_answer()



#Test cases for searching on Google

@pytest.mark.parametrize("query", [
    "search on google for cats",
    "find information on pytest on google",
])
def test_web_browser_google_search(query):
    web_browser(query + " on google")


# Test cases for searching on YouTube
@pytest.mark.parametrize("query", [
    "python tutorials on youtube",
    "cute cat videos on youtube",
])
def test_web_browser_youtube_search(query):
    web_browser(query + " on youtube")


# Test the web_browser function

def test_web_browser_open_python_status():
    # Test to open Python status website
    query = "open python status"
    web_browser(query)
    assert "opening python status" in pytest.captured_output()

def test_web_browser_open_facebook():
    # Test to open Facebook
    query = "open facebook"
    web_browser(query)
    assert "opening facebook" in pytest.captured_output()


#  Test the spotify_music function 

def test_spotify_music_open_spotify():
    # Test open Spotify
    query = "open spotify"
    spotify_music(query)
    assert "opening spotify" in pytest.captured_output()

def test_spotify_music_search_song():
    # Test search and play a song
    query = "search song coldplay"
    spotify_music(query)
    assert "searched song is playing" in pytest.captured_output()


# Test the openai_gpt function

def test_openai_gpt_in_detail():
    # Test to provide a detailed answer
    query = "what is the history of openai gpt?"
    openai_gpt(query)
    assert "openai gpt" in pytest.captured_output()

def test_openai_gpt_short_answer():
    # Test to provide a short answer
    query = "how to write an essay?"
    openai_gpt(query)
    assert "write an essay" in pytest.captured_output()



if __name__ == "__main__":
    main()
