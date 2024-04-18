import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TextParentNode(unittest.TestCase):
    def test_parent_node_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(actual, expected)

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                ParentNode("span", [LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text")]),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = "<p><span>Normal text<i>italic text</i></span>Normal text</p>"
        self.assertEqual(actual, expected)

    def test_two_levels_nested_parent_nodes(self):
        node = ParentNode(
            "p",
            [
                ParentNode("span", [LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text"),
                                    ParentNode("span", [
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text")])
                                    ]),
                LeafNode(None, "Normal text"),
            ],
        )
        actual = node.to_html()
        expected = "<p><span>Normal text<i>italic text</i><span>Normal text<i>italic text</i></span></span>Normal text</p>"
        self.assertEqual(actual, expected)
