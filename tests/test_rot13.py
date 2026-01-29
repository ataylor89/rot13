from rot13 import rot13
from tests import test_data_path
from unittest import TestCase

class TestRot13(TestCase):

    def test_rot13(self):
        with open(test_data_path / 'input.txt', 'r') as file:
            input = file.read()
        with open(test_data_path / 'expected.txt', 'r') as file:
            expected = file.read()
        assert rot13(input) == expected
        assert rot13(expected) == input
