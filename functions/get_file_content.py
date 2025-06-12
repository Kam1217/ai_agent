import os

def get_file_content(working_directory, file_path):


    file_directory_path = os.path.abspath(os.path.join(working_directory, file_path))   

    if not os.path.isfile(file_directory_path):
        return f'Error: File not found or is not regular file: "{file_directory_path}"'
    
    if not os.path.abspath(file_directory_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outsidee the permitted working directory'
    
    try:
        max_char = 1000
        
        with open(file_directory_path, "r") as f:
            file_content_str = f.read(max_char)
            if f.read(1):
               file_content_str += f'[...File "{file_path}" truncated at 1000 characters]'
        return file_content_str

    except Exception as e:
        return f"Error: {e}"
