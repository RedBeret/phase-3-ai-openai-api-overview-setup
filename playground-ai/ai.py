import os
from openai import OpenAI
from openai import OpenAI

client = OpenAI()
from dotenv import load_dotenv, find_dotenv
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


# messages = [{"role": "user", "content": "What is the capital of New York?"}]
# try:
#     response = client.chat.completions.create(model="gpt-3.5-turbo",
#     messages=messages,
#     temperature=0)

#     print(response.choices[0].message.content)
# except Exception as e:
#     print(e)



# Basic Prompt Function
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    
    # Here's where the API call is made
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=temperature)
    
    # Print statement to view the response object (for debugging purposes)
    # print(response)  # Uncomment this line for debugging

    # Return the content of the response from the assistant
    return response.choices[0].message.content

# Context Aware Function
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=temperature)
    
    # Return the content of the response from the assistant
    return response.choices[0].message.content

# This section is commented out to prevent unnecessary API calls when importing this module.
# Instead, you will use the `app.py` to interact with these functions.
# messages = [{"role": "user", "content": "What is the capital of New York?"}]
# try:
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         temperature=0,
#     )
#     print(response.choices[0].message["content"])
# except Exception as e:
#     print(e)