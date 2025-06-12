import unittest

def run_all_tests():

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests', pattern='test_*.py')

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return result

if __name__ == '__main__':
    run_all_tests()