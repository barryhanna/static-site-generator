block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def block_to_block_type(markdown):
    if markdown.startswith('#'):
        return block_type_heading
    elif markdown.startswith('```') and markdown.endswith('```'):
        return block_type_code
    elif markdown.startswith('>'):
        for line in markdown.split("\n"):
            if not line.startswith('>'):
                return block_type_paragraph

        return block_type_quote
    elif markdown.startswith("* ") or markdown.startswith("- "):
        marker = markdown[0]
        for line in markdown.split("\n"):
            if not line.startswith(f"{marker} "):
                return block_type_paragraph
        return block_type_unordered_list
    elif markdown.startswith("1. "):
        marker = markdown[0]
        list_items = markdown.split("\n")
        for i, item in enumerate(list_items):
            if not item.startswith(f"{i+1}. "):
                return block_type_paragraph
        return block_type_ordered_list
    else:
        return block_type_paragraph
