import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlNodeOne = HTMLNode("a", "link", None, {"href": "https://boot.dev"})
        htmlNodeTwo = HTMLNode("a", "link", None, {"href": "https://boot.dev"})
        self.assertEqual(htmlNodeOne, htmlNodeTwo)

    def test_to_html(self):
        actual = HTMLNode("a", "link", None, {
                               "href": "https://boot.dev"}).props_to_html()
        expected = f"href=https://boot.dev"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
