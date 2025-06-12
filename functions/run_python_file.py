import os 
import subprocess

def run_python_file(working_directory, file_path):
    
    file_directory_path = os.path.abspath(os.path.join(working_directory, file_path))   

    if not os.path.abspath(file_directory_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_directory_path):
        return f'Error: File "{file_path}" not found"'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_directory, timeout=30)
        stdout_output = result.stdout.decode()
        stderr_output = result.stderr.decode()
        result_output = f"STDOUT: {stdout_output}\nSTDERR: {stderr_output}"

        if stdout_output == "" and stderr_output == "":
            return "No output produced."
        if result.returncode is not 0:
            return f"{result_output}\nProcess exited with code {result.returncode}"
        return result_output
        
    except Exception as e:
        return f"Error: executing Python file: {e}"