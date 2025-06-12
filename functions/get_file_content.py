import os

def get_file_content(working_directory, file_path):

    if file_path is None:
        file_directory_path = os.path.abspath(working_directory)
    else:
        file_directory_path = os.path.abspath(os.path.join(working_directory, file_path))   

    if not os.path.isfile(file_directory_path):
        return f'Error: File not found or is not regular file: "{file_directory_path}"'
    
    if not os.path.abspath(file_directory_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outsidee the permitted working directory'