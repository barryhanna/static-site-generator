def generate_page(from_path, template_path, dest_path):
    pass


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith('# '):
            return line.split('# ')[1]
    raise Exception("No title found in markdown document")
