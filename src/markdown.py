import re

from blocktype import *
from parentnode import ParentNode
from textnode import text_to_textnodes, text_node_to_html_node


def markdown_to_blocks(markdown):
    blocks = re.split(r"\n{2,}", markdown)
    return [block.strip() for block in blocks if block.strip() != '']


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    if block_to_block_type(block) == block_type_quote:
        return quote_to_html_node(block)
    elif block_to_block_type(block) == block_type_unordered_list:
        return ulist_to_html_node(block)
    elif block_to_block_type(block) == block_type_ordered_list:
        return olist_to_html_node(block)
    elif block_to_block_type(block) == block_type_code:
        return code_to_html_node(block)
    elif block_to_block_type(block) == block_type_heading:
        return heading_to_html_node(block)
    elif block_to_block_type(block) == block_type_paragraph:
        return paragraph_to_html_node(block)


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


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
