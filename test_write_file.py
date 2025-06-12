import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    
    def test_write_simple_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        self.assertIn("28 characters written", result)
        self.assertIn("Successfully wrote", result)
    
    def test_write_nested_file(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        self.assertIn("26 characters written", result)
        self.assertIn("Successfully wrote", result)
    
    def test_reject_outside_directory(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        self.assertIn("Error:", result)
        self.assertIn("outside the permitted working directory", result)

if __name__ == '__main__':
    unittest.main()


