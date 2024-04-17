class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self):
        return self.text == self.text_type == self.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
