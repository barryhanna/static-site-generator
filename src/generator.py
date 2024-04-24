from htmlnode import HTMLNode
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")
    with open(from_path) as markdown_file, open(template_path) as template_file, open(dest_path, 'w') as output_file:
        markdown = markdown_file.read()
        template = template_file.read()
        print(f"TEMPLATE: {template}")
        html = HTMLNode.markdown_to_html_node(markdown)
        print(f"HTML: \n{html}")
        title = extract_title(markdown)
        print(f"TITLE: \n{title}")
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)
        # if not os.path.exists(output_file):
        #     os.makedirs(output_file)
        output_file.writelines(template)


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith('# '):
            return line.split('# ')[1]
    raise Exception("No title found in markdown document")
