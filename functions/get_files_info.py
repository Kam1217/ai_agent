import os

def get_files_info(working_directory, directory=None):
    
    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    results = []
    for item in os.listdir(directory):
        path_to_item = os.path.join(directory, item)
        
        file_size = os.path.getsize(path_to_item)
        is_dir = os.path.isdir(path_to_item)

        line = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
        results.append(line)

    return "\n".join(results)
