import re
from htmlnode import HTMLNode
from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
text_types = [text_type_text, text_type_bold, text_type_italic,
              text_type_code, text_type_link, text_type_image]


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type})"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(
                "Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(
                    TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})")
            if len(sections) != 2:
                raise ValueError(
                    "Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(
                    TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(image[0], text_type_image, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(
                TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})")
            if len(sections) != 2:
                raise ValueError(
                    "Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(
                    TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(
                TextNode(original_text, text_type_link))
    return new_nodes


def has_image_link(str):
    return len(TextNode.extract_markdown_images(str)) > 0


def extract_markdown_images(text):
    markdown_image_re = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(markdown_image_re, text)
    return matches


def extract_markdown_links(text):
    markdown_image_re = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(markdown_image_re, text)
    return matches


def markdown_to_blocks(markdown):
    blocks = re.split(r"\n{2,}", markdown)
    return [block.strip() for block in blocks if block.strip() != '']


def text_node_to_html_node(text_node):
    if (text_node.text_type == "text"):
        return LeafNode(None, text_node.text, text_node.text_type)
    if (text_node.text_type == "bold"):
        return LeafNode("b", text_node.text)
    if (text_node.text_type == "italic"):
        return LeafNode("i", text_node.text)
    if (text_node.text_type == "code"):
        return LeafNode("code", text_node.text)
    if (text_node.text_type == "link"):
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if (text_node.text_type == "image"):
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("TextNode does not have a supported text type")


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(
        nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(
        nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(
        nodes, "`", text_type_code)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
