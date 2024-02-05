# open AI engin code file
import openai
import time


"""   RETURN  RESULT  FROM OPEN AI   """

# Enter open AI  key
def openai_key():
    try:
        key = 'OPEN AI API KEY'  # Enter api key
        return key
    except Exception:
        print("Please enter your openai api key in   ' project/open_ai/__init__.py '  file to use openAI service")


# function to get response to open AI 'ChatGPT'
def openai_ask(query):
    openai.api_key = openai_key()
    try:
        if query:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query},],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
        return response.choices[0].message.content
    except openai.error.RateLimitError as e:
        print(f"Rate limit exceeded. Waiting for 20 seconds.", e)    # Handle rate limit error by waiting and retrying
        time.sleep(20)
        return openai_ask(query)
    except Exception:
        pass


# test functions...
if __name__ == "__main__":
    task = openai_ask("who is yogi adityanath")
    print(task)
