from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

if __name__ == "__main__":
    # print(f"Should print file info result: {get_files_info('calculator', '.')}")
    # print(f"Should print file info result: {get_files_info('calculator', 'pkg')}")
    # print(f"Should print file info error: {get_files_info('calculator', '/bin')}")
    # print(f"Should print file info error: {get_files_info('calculator', '../')}")

    # print(f"Should print file content: {get_file_content("calculator", "main.py")}")
    # print(f"Should print file content: {get_file_content("calculator", "pkg/calculator.py")}")
    print(f"Should print file content up to 10000 char: {get_file_content("calculator", "lorem.txt")}")
    # print(f"Should print file content error:{ get_file_content("calculator", "/bin/cat")}")