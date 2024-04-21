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

    def test_split_nodes_delimiter_text(self):
        node = TextNode(
            "This is a text node", "text")
        actual = TextNode.split_nodes_delimiter([node], None, node.text_type)
        expected = [
            TextNode("This is a text node", TextNode.text_type_text),
        ]
        self.assertEqual(actual, expected)

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

    # def test_split_nodes_delimiter_link(self):
    #     node = TextNode(
    #         "This is text with a [link](https://boot.dev) word", "link")
    #     actual = TextNode.split_nodes_delimiter([node], "()", node.text_type)
    #     expected = [
    #         TextNode("This is text with a ", TextNode.text_type_text),
    #         TextNode("italic block", TextNode.text_type_italic),
    #         TextNode(" word", TextNode.text_type_text)
    #     ]
    #     self.assertEqual(actual, expected)

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        actual = TextNode.extract_markdown_images(text)
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(actual, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        actual = TextNode.extract_markdown_links(text)
        expected = [("link", "https://www.example.com"),
                    ("another", "https://www.example.com/another")]
        self.assertEqual(actual, expected)

    def test_split_nodes_images(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                        TextNode.text_type_text,
                        )
        actual = TextNode.split_nodes_images([node])
        expected = [
            TextNode("This is text with an ", TextNode.text_type_text),
            TextNode("image", TextNode.text_type_image,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextNode.text_type_text),
            TextNode(
                "second image", TextNode.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(actual, expected)

    def test_split_nodes_link(self):
        node = TextNode("This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                        TextNode.text_type_text,
                        )
        actual = TextNode.split_nodes_link([node])
        expected = [
            TextNode("This is text with an ", TextNode.text_type_text),
            TextNode("link", TextNode.text_type_link,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextNode.text_type_text),
            TextNode(
                "second link", TextNode.text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
