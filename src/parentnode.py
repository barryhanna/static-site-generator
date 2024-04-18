from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        self.tag = tag
        self.children = children

    def to_html(self):
        if not self.tag:
            raise ValueError("A tag is required")
        if not self.children:
            raise ValueError("ParentNode must have children")

        childHTML = ""
        for node in self.children:
            childHTML += node.to_html()

        return f"<{self.tag}>{childHTML}</{self.tag}>"
