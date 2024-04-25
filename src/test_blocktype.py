import unittest

from blocktype import *


class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        actual = block_to_block_type("This is some paragraph text")
        expected = block_type_paragraph
        self.assertEqual(actual, expected)

    def test_block_to_block_type_code(self):
        actual = block_to_block_type("```print('Hello, world')```")
        expected = block_type_code
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading(self):
        actual = block_to_block_type("# Heading 1")
        expected = block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading2(self):
        actual = block_to_block_type("## Heading 2")
        expected = block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list(self):
        actual = block_to_block_type(
            "- Buy milk\n- Buy bread\n- post letter")
        expected = block_type_unordered_list
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list_alt(self):
        actual = block_to_block_type(
            "* Buy milk\n* Buy bread\n* post letter")
        expected = block_type_unordered_list
        self.assertEqual(actual, expected)

    def test_block_to_block_type_ordered_list(self):
        actual = block_to_block_type(
            "1. Buy milk\n2. Buy bread\n3. post letter")
        expected = block_type_ordered_list
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
