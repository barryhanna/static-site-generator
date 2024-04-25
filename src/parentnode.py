from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A tag is required")
        if not self.children:
            raise ValueError("ParentNode must have children")

        childHTML = ""
        for node in self.children:
            childHTML += node.to_html()

        return f"<{self.tag}{self.props_to_html()}>{childHTML}</{self.tag}>"
