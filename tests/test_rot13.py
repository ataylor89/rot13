from tests import project_root
from rot13 import rot13
from unittest import TestCase

class TestRot13(TestCase):

    @classmethod
    def setUpClass(cls):
        input_path = project_root / 'tests' / 'test_data' / 'input.txt'
        with open(input_path, 'r') as file:
            cls.input = file.read()
        expected_path = project_root / 'tests' / 'test_data' / 'expected.txt'
        with open(expected_path, 'r') as file:
            cls.expected = file.read()

    def test_rot13(self):
        assert rot13(self.input) == self.expected
        assert rot13(self.expected) == self.input
