import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
verbose = "--verbose" in sys.argv

if len(sys.argv) == 1:
    print("No prompt provided")
    sys.exit(1)
if verbose:
    prompt = " ".join(sys.argv[1:-1])
else:
    prompt = " ".join(sys.argv[1:])

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description="Returns the contents of a specified file up to 1000 characters",
    parameters=types.Schema(
        type = types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read file contents from, relative to the working directory. If file is not provided, return an error specifying the file does not exist.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description="Executes Python files with optional arguments",
    parameters= types.Schema(
        type = types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run the python script from, relative to the working directory. If file is not provided or is not a python file, return an error specifying the file does not exist.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description="Overwrites the contents of a specified file. If the file does not exist it creates it with the contents instead",
    parameters= types.Schema(
        type = types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file which will have the overwritten content, relative to the working directory. If file is not provided it creates the files with the specified contents",

            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to overwrite a file with. If a file does not exists create a file with the contents instead"
            )
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]
response = client.models.generate_content(model='gemini-2.0-flash-001', contents= messages, config= types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))

if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if response.function_calls:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
else:
    print(response.text)


