from htmlnode import HTMLNode
from leafnode import LeafNode


class TextNode():
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
    text_types = [text_type_text, text_type_bold, text_type_italic,
                  text_type_code, text_type_link, text_type_image]

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self, text_node):
        if not (text_node.text_type in self.text_types):
            raise Exception("TextNode does not have a supported text type")
        if (text_node.text_type == "text"):
            return LeafNode(None, text_node.value)
        if (text_node.text_type == "bold"):
            return LeafNode("b", text_node.value)
        if (text_node.text_type == "italic"):
            return HTMLNode("i", text_node.value)
        if (text_node.text_type == "code"):
            return HTMLNode("code", text_node.value)
        if (text_node.text_type == "link"):
            return HTMLNode("a", text_node.value, {"href": text_node.props.href})
        if (text_node.text_type == "image"):
            return HTMLNode("img", "", {"src": text_node.url, "alt": text_node.value})

    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, ttc):
        new_nodes = []
        for old_node in old_nodes:
            node = old_node.text.split(delimiter)
            if len(node) < 3:
                raise Exception(
                    "Unbalanced delimiter. Must have start and end delimiter")
            if type(node) != TextNode:
                new_nodes.append(node)
                continue

            # only process non-empty strings
            for part in node:
                if part:
                    new_nodes.append(TextNode(None, part, ttc))

        return new_nodes
