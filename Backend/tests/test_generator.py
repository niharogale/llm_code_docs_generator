import unittest
from src.core.generator import DocumentationGenerator

class TestDocumentationGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = DocumentationGenerator()

    def test_generate_docs(self):
        # Example input for testing
        codebase = {
            'functions': [
                {'name': 'add', 'description': 'Adds two numbers'},
                {'name': 'subtract', 'description': 'Subtracts one number from another'}
            ]
        }
        expected_output = "## Documentation\n\n### Functions\n\n- **add**: Adds two numbers\n- **subtract**: Subtracts one number from another\n"
        output = self.generator.generate_docs(codebase)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()