import unittest

from blocktype import BlockType


class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        actual = BlockType.block_to_block_type("This is some paragraph text")
        expected = BlockType.block_type_paragraph
        self.assertEqual(actual, expected)

    def test_block_to_block_type_code(self):
        actual = BlockType.block_to_block_type("```print('Hello, world')```")
        expected = BlockType.block_type_code
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading(self):
        actual = BlockType.block_to_block_type("# Heading 1")
        expected = BlockType.block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading2(self):
        actual = BlockType.block_to_block_type("## Heading 2")
        expected = BlockType.block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list(self):
        actual = BlockType.block_to_block_type(
            "- Buy milk\n- Buy bread\n- post letter")
        expected = BlockType.block_type_unordered_list
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list_alt(self):
        actual = BlockType.block_to_block_type(
            "* Buy milk\n* Buy bread\n* post letter")
        expected = BlockType.block_type_unordered_list
        self.assertEqual(actual, expected)

    def test_block_to_block_type_ordered_list(self):
        actual = BlockType.block_to_block_type(
            "1. Buy milk\n2. Buy bread\n3. post letter")
        expected = BlockType.block_type_ordered_list
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
