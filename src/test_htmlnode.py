import unittest

from htmlnode import *
from markdown import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlNodeOne = HTMLNode("a", "link", None, {"href": "https://boot.dev"})
        htmlNodeTwo = HTMLNode("a", "link", None, {"href": "https://boot.dev"})
        self.assertEqual(htmlNodeOne, htmlNodeTwo)

    def test_to_html(self):
        actual = HTMLNode("a", "link", None, {
                               "href": "https://boot.dev"}).props_to_html()
        expected = f" href=\"https://boot.dev\""
        self.assertEqual(expected, actual)

    def test_markdown_to_html_blockquote(self):
        actual = markdown_to_html_blockquote(
            "> This is a\n> blockquote. There\n> Are many lines")
        expected = "<blockquote>This is a\nblockquote. There\nAre many lines</blockquote>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_ul(self):
        actual = markdown_to_html_ul(
            "* This is a\n* list. There\n* Are many lines")
        expected = "<ul><li>This is a</li><li>list. There</li><li>Are many lines</li></ul>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_ol(self):
        actual = markdown_to_html_ol(
            "1. This is a\n2. list. There\n3. Are many lines")
        expected = "<ol><li>This is a</li><li>list. There</li><li>Are many lines</li></ol>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_code(self):
        actual = markdown_to_html_code(
            "```print('Hello, world!')```")
        expected = "<pre><code>print('Hello, world!')</code></pre>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_h1(self):
        actual = markdown_to_html_heading(
            "#Heading 1")
        expected = "<h1>Heading 1</h1>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_h2(self):
        actual = markdown_to_html_heading(
            "##Heading 2")
        expected = "<h2>Heading 2</h2>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_h6(self):
        actual = markdown_to_html_heading(
            "######Heading 6")
        expected = "<h6>Heading 6</h6>"
        self.assertEqual(actual, expected)

    def test_markdown_to_html_paragraph(self):
        actual = markdown_to_html_paragraph(
            "This is just a paragraph")
        expected = "<p>This is just a paragraph</p>"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
