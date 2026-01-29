from rot13 import rot13
from unittest import TestCase

class TestRot13(TestCase):

    def test_rot13(self):
        with open('tests/test_data/input.txt', 'r') as file:
            input = file.read()
        with open('tests/test_data/expected.txt', 'r') as file:
            expected = file.read()
        assert rot13(input) == expected
        assert rot13(expected) == input
