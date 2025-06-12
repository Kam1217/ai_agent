import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

verbose = "--verbose" in sys.argv

if len(sys.argv) == 1:
    print("No prompt provided")
    sys.exit(1)

if verbose:
    prompt = " ".join(sys.argv[1:-1])
else:
    prompt = " ".join(sys.argv[1:])

messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]
response = client.models.generate_content(model='gemini-2.0-flash-001', contents= messages)

if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)


