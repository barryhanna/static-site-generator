from htmlnode import markdown_to_html_node
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")
    with open(from_path) as markdown_file, open(template_path) as template_file, open(dest_path, 'w') as output_file:
        markdown = markdown_file.read()
        template = template_file.read()
        html = markdown_to_html_node(markdown)
        title = extract_title(markdown)
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)
        output_file.writelines(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        file_path = os.path.join(dir_path_content, file)
        print(file_path)
        if os.path.isfile(file_path) and file.endswith('.md'):
            input_file = os.path.join(dir_path_content, file)
            output_file = os.path.join(
                dest_dir_path, file.replace(".md", ".html"))
            generate_page(input_file, template_path,
                          output_file)
        elif os.path.isdir(file_path):
            input_dir = os.path.join(dir_path_content, file)
            output_dir = os.path.join(dest_dir_path, file)
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            generate_pages_recursive(input_dir, template_path, output_dir)


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith('# '):
            return line.split('# ')[1]
    raise Exception("No title found in markdown document")
