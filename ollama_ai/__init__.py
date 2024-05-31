import time
import replicate
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()


"""   RETURN  RESULT  FROM OLLAMA AI   """

try:
    # accessing api key
    os.environ["REPLICATE_API_TOKEN"] = os.getenv('OLLAMA_AI_API_KEY')
except Exception:
    print("Please fill your OLLAMA_AI_API_KEY in your .env file")

def ollama(prompt_input):
    # Prompts
    pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."

    # Generate LLM response
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                           # LLM model
                           input={"prompt": f"{prompt_input} Assistant: ",  # Prompts
                                  "temperature": 0.1, "top_p": 0.9, "max_length": 500,
                                  "repetition_penalty": 1})  # Model parameters

    # output = replicate.run('wizardlm/wizardlm-70b:latest',
    #                        input={"prompt": f"{prompt_input} Assistant: ",
    #                               "temperature": 0.1, "top_p": 0.9,
    #                               "max_length": 500, "repetition_penalty": 1})

    full_response = ""
    for item in output:
      full_response += item
    return full_response



# test function
if __name__ == "__main__":
    task = ollama("what is js")
    print(task)











