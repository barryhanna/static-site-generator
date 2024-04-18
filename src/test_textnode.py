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

    def test_split_nodes_delimiter_code(self):
        node = TextNode(
            "This is text with a `code block` word", "code")
        actual = TextNode.split_nodes_delimiter([node], "`", node.text_type)
        expected = [
            TextNode("This is text with a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(" word", TextNode.text_type_text)
        ]
        self.assertEqual(actual, expected)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode(
            "This is text with a **bold block** word", "bold")
        actual = TextNode.split_nodes_delimiter(
            [node], "**", node.text_type_bold)
        expected = [
            TextNode("This is text with a ", TextNode.text_type_text),
            TextNode("bold block", TextNode.text_type_bold),
            TextNode(" word", TextNode.text_type_text)
        ]
        self.assertEqual(actual, expected)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode(
            "This is text with a *italic block* word", "italic")
        actual = TextNode.split_nodes_delimiter([node], "*", node.text_type)
        expected = [
            TextNode("This is text with a ", TextNode.text_type_text),
            TextNode("italic block", TextNode.text_type_italic),
            TextNode(" word", TextNode.text_type_text)
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
