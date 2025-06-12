import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

class TestGetFileInfo(unittest.TestCase):
    def test_lists_calculator_root(self):
        result = get_files_info('calculator', '.')
        self.assertNotIn("Error:", result)
    
    def test_lists_pkg_directory(self):
        result = get_files_info('calculator', 'pkg')
        self.assertNotIn("Error:", result)
    
    def test_rejects_bin_directory(self):
        result = get_files_info('calculator', '/bin')
        self.assertIn("Error:", result)
    
    def test_rejects_parent_directory(self):
        result = get_files_info('calculator', '../')
        self.assertIn("Error:", result)


class TestGetFileContent(unittest.TestCase):
   
    def test_truncates_large_file(self):
        result = get_file_content("calculator", "lorem_20K_char.txt")
        self.assertTrue(result.endswith('[...File "lorem_20K_char.txt" truncated at 1000 characters]'))
        content_part = result[:-len('[...File "lorem_20K_char.txt" truncated at 1000 characters]')]
        self.assertEqual(len(content_part), 1000)
    
    def test_reads_main_py(self):
        result = get_file_content("calculator", "main.py")
        self.assertIn("def main():", result)
        self.assertFalse(result.startswith("Error:"))
    
    def test_reads_calculator_py(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertIn("self._apply_operator(operators, values)", result)
        self.assertFalse(result.startswith("Error:"))
    
    def test_rejects_outside_directory(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertIn("Error:", result)

if __name__ == "__main__":
    unittest.main()