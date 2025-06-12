import os

def write_file(working_directory, file_path, content):
    
    file_directory_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.abspath(file_directory_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
      
    try:
        directory = os.path.dirname(file_directory_path)
        os.makedirs(directory, exist_ok=True)

        with open(file_directory_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  
    except Exception as e:
        return f"Error: {e}"