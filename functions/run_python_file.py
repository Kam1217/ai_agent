import os 

def run_python_file(working_directory, file_path):
    
    file_directory_path = os.path.abspath(os.path.join(working_directory, file_path))   

    if not os.path.isfile(file_directory_path):
        return f'Error: File "{file_path} not found"'
    
    if not os.path.abspath(file_directory_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'