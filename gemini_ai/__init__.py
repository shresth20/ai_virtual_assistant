import textwrap
import os
from dotenv import load_dotenv
import google.generativeai as genai
# Load environment variables from the .env file
load_dotenv()


# Function to get API key for Google Generative AI
def get_google_api_key():
    try:
        # Fetch your Google API key from environment variables or wherever it's stored
        return  os.getenv('GOOGLE_API_KEY')
    except Exception:
        print("Please fill your GOOGLE_API_KEY in your .env file")

# Function to ask a question to the Gemni model
def ask_gemini(question):
    # Configure the API key
    genai.configure(api_key=get_google_api_key())
    # Selecting an appropriate model
    model = genai.GenerativeModel('gemini-pro')
    # Generate content using the model
    response = model.generate_content(question)
    text =  response._result.candidates[0].content.parts[0].text
    return textwrap.dedent( text.strip().replace('*', ''))


# Test the function
if __name__ == "__main__":
    question = "who is yogi adityanath"
    response = ask_gemini(question)
    # print(response.result.candidates[0].content.parts[0].text)
    print(response)
