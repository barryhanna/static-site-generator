import re

from blocktype import BlockType


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = []
        if not self.props:
            return ''
        for key, value in self.props.items():
            props.append(f"{key}=\"{value}\"")
        return ' ' + ' '.join(props)

    def __repr__(self):
        return f"{self.value} {self.tag} {self.children} {self.props}"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


def markdown_to_blocks(markdown):
    blocks = re.split(r"\n{2,}", markdown)
    return [block.strip() for block in blocks if block.strip() != '']


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = ""
    for block in blocks:
        if BlockType.block_to_block_type(block) == BlockType.block_type_quote:
            html_blocks += markdown_to_html_blockquote(block)
        elif BlockType.block_to_block_type(block) == BlockType.block_type_unordered_list:
            html_blocks += markdown_to_html_ul(block)
        elif BlockType.block_to_block_type(block) == BlockType.block_type_ordered_list:
            html_blocks += markdown_to_html_ol(block)
        elif BlockType.block_to_block_type(block) == BlockType.block_type_code:
            html_blocks += markdown_to_html_code(block)
        elif BlockType.block_to_block_type(block) == BlockType.block_type_heading:
            html_blocks += markdown_to_html_heading(block)
        elif BlockType.block_to_block_type(block) == BlockType.block_type_paragraph:
            html_blocks += markdown_to_html_paragraph(block)

    return f"<div>{html_blocks}</div>"


def markdown_to_html_blockquote(markdown):
    text = markdown.replace("> ", "")
    return f"<blockquote>{text.strip()}</blockquote>"


def markdown_to_html_paragraph(markdown):
    return f"<p>{markdown.strip()}</p>"


def markdown_to_html_heading(markdown):
    heading_size = 0
    for char in markdown:
        if char == "#":
            heading_size += 1
    markdown = markdown.replace(f"{"#" * heading_size}", "")
    return f"<h{heading_size}>{markdown.strip()}</h{heading_size}>"


def markdown_to_html_code(markdown):
    markdown = markdown.replace("```", "")
    return f"<pre><code>{markdown.strip()}</code></pre>"


def markdown_to_html_ul(markdown):
    marker = markdown[0]
    markdown = [item.replace(f"{marker} ", "")
                for item in markdown.split("\n")]
    list_html = ""
    for item in markdown:
        list_html += f"<li>{item.strip()}</li>"
    return f"<ul>{list_html}</ul>"


def markdown_to_html_ol(markdown):
    markdown = [item[3:] for item in markdown.split("\n")]
    list_html = ""
    for item in markdown:
        list_html += f"<li>{item}</li>"
    return f"<ol>{list_html}</ol>"
