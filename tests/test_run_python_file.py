import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    
    def test_run_main_without_args(self):
        result = run_python_file("calculator", "main.py")
        
        self.assertIn("STDOUT:", result)
        self.assertIn("Calculator App", result)
        self.assertIn("Usage: python main.py", result)
        self.assertIn('Example: python main.py "3 + 5"', result)
        self.assertNotIn("Error:", result)

    def test_run_tests_file(self):
        result = run_python_file("calculator", "tests.py")
    
        self.assertIn("STDOUT:", result)
        self.assertIn("STDERR:", result)
        self.assertIn("Ran", result) 
        self.assertTrue("OK" in result or "FAILED" in result)
        self.assertNotIn("Error: executing Python file", result)
    
    def test_file_outside_working_directory(self):
        result = run_python_file("calculator", "../main.py")
        
        self.assertIn("Cannot execute", result)
        self.assertIn("outside the permitted working directory", result)
    
    def test_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        
        self.assertIn("File \"nonexistent.py\" not found", result)
    
    def test_non_python_file(self):
        result = run_python_file("calculator", "lorem.txt")
        
        self.assertIn("is not a Python file", result)

if __name__ == '__main__':
    unittest.main()