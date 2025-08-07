import unittest
from src.core.analyzer import CodeAnalyzer

class TestCodeAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = CodeAnalyzer()

    def test_analyze_code(self):
        code = """
        def add(a, b):
            \"\"\"Adds two numbers together.\"\"\"
            return a + b
        """
        expected_output = {
            'function_name': 'add',
            'docstring': 'Adds two numbers together.',
            'parameters': ['a', 'b'],
            'return_type': 'int'
        }
        result = self.analyzer.analyze_code(code)
        self.assertEqual(result, expected_output)

    def test_analyze_empty_code(self):
        code = ""
        expected_output = {}
        result = self.analyzer.analyze_code(code)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()