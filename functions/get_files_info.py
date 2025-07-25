import os

def get_files_info(working_directory, directory=None):

    if directory is None:
        directory_path = os.path.abspath(working_directory)
    else:
        directory_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not os.path.isdir(directory_path):
        return f'Error: "{directory}" is not a directory'
    
    if not os.path.abspath(directory_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    try:
        results = []
        for item in os.listdir(directory_path):
            path_to_item = os.path.join(directory_path, item)
        
            file_size = os.path.getsize(path_to_item)
            is_dir = os.path.isdir(path_to_item)

            line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            results.append(line)

        return "\n".join(results)
    except Exception as e:
        return f"Error: {e}"
