import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'bold')
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode('Text node', 'italic')
        self.assertEqual(node.url, None)

    def test_not_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node, but different', 'bold')
        self.assertNotEqual(node, node2)

    def test_split_nodes_delimiter(self):
        node = TextNode(
            "This is text with a `code block` word", "code")
        actual = TextNode.split_nodes_delimiter([node], "`", node.text_type)
        expected = [
            TextNode(None, "This is a text with a", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(None, " word", TextNode.text_type_text)
        ]
        print(f"ACTUAL: {actual}")
        print(f"EXPECTED: {expected}")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
