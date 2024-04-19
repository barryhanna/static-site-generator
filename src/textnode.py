import re
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
        return f"TextNode({self.text},{self.text_type})"

    def text_node_to_html_node(self, text_node):
        if not (text_node.text_type in self.text_types):
            raise Exception("TextNode does not have a supported text type")
        if (text_node.text_type == "text"):
            return LeafNode(text_node.value, text_node.type)
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
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for old_node in old_nodes:
            if type(old_node) != TextNode:
                new_nodes.append(old_node)
                continue

            if text_type == "text":
                new_nodes.append(old_node)
                continue

            node = old_node.text.split(delimiter)
            # ['','some text','']
            if len(node) < 3:
                raise Exception(
                    "Unbalanced delimiter. Must have start and end delimiter")

            # only process non-empty strings
            if node[0]:
                new_nodes.append(TextNode(node[0], "text"))
            if node[1]:
                new_nodes.append(TextNode(node[1], text_type))
            if node[2]:
                new_nodes.append(TextNode(node[2], "text"))

        return new_nodes

    @staticmethod
    def split_nodes_images(old_nodes):
        new_nodes = []
        for node in old_nodes:
            extracted_image_nodes = TextNode.extract_markdown_images(node.text)
            # [("image","https://www.someimage.com"),("image","https://www.someimage.com")]
            # if no image links are extracted, just add the node to new_nodes
            if not extracted_image_nodes:
                new_nodes.append(node)
                continue
            # TODO:
            for image_node in extracted_image_nodes:
                # reconstruct markdown image link to use for split
                image_link = f"![{image_node[0]}]({image_node[1]})"
                # split the node text on image link
                text_nodes = node.text.split(image_link, 1)

                # left-hand node, only do if node is not empty
                if text_nodes[0]:
                    new_nodes.append(
                        TextNode(text_nodes[0], TextNode.text_type_text))
                # add the image link node
                new_nodes.append(
                    TextNode(image_node[0], "image", image_node[1]))

                # right-hand node
                if text_nodes[1]:
                    new_nodes.append(
                        TextNode(text_nodes[1], TextNode.text_type_text))
                    # if TextNode.has_image_link(text_nodes[1]):
                    #     TextNode.split_nodes_images(
                    #         [TextNode(text_nodes[1], TextNode.text_type_text)])
                    # else:
                    #     new_nodes.append(
                    #         TextNode(text_nodes[1], TextNode.text_type_text))

        return new_nodes

    # Check if a given string contains a markdown image link

    @ staticmethod
    def has_image_link(str):
        return len(TextNode.extract_markdown_images(str)) > 0

    @ staticmethod
    def extract_markdown_images(text):
        markdown_image_re = r"!\[(.*?)\]\((.*?)\)"
        matches = re.findall(markdown_image_re, text)
        return matches

    @ staticmethod
    def extract_markdown_links(text):
        markdown_image_re = r"\[(.*?)\]\((.*?)\)"
        matches = re.findall(markdown_image_re, text)
        return matches
