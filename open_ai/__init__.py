# open AI engin code file
import openai
import time
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

"""   RETURN  RESULT  FROM OPEN AI   """

# Enter open AI  key
def openai_key():
    try:
        return os.getenv('OPEN_AI_API_KEY')
    except Exception:
        print("Please fill your OPEN_AI_API_KEY in  .env file")


# function to get response to open AI 'ChatGPT'
def openai_ask(query):
    openai.api_key = openai_key()
    try:
        if query:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
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
