import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leafNodeOne = LeafNode("p", "Hello, this is a paragraph", {
                               "style": "color: red"})
        leafNodeTwo = LeafNode("p", "Hello, this is a paragraph", {
                               "style": "color: red"})
        self.assertEqual(leafNodeOne, leafNodeTwo)

    def test_to_html(self):
        actual = LeafNode("a", "Link", {"href": "https://boot.dev"}).to_html()
        expected = "<a href=\"https://boot.dev\">Link</a>"
        self.assertEqual(actual, expected)

    def test_to_html_no_props(self):
        actual = LeafNode("p", "This paragraph has no props", {}).to_html()
        expected = "<p>This paragraph has no props</p>"
        self.assertEqual(actual, expected)

    def test_no_tag(self):
        actual = LeafNode(None, "This paragraph has no tag", {}).to_html()
        expected = "This paragraph has no tag"
        self.assertEqual(actual, expected)
