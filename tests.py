from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print(f"Should print result: {get_files_info('calculator', '.')}")
    print(f"Should print result: {get_files_info('calculator', 'pkg')}")
    print(f"Should print error: {get_files_info('calculator', '/bin')}")
    print(f"Should print error: {get_files_info('calculator', '../')}")