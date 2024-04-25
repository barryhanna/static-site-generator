import os
import shutil
from generator import generate_pages_recursive

dir_path = os.path.dirname(os.path.realpath(__file__))
INPUT_DIR = os.path.join(dir_path, "..", "static")
OUTPUT_DIR = os.path.join(dir_path, "..", "public")


def clean_output_dir():
    print("Cleaning out dir...")
    full_path = os.path.join(dir_path, "..", "public")
    if os.path.exists(full_path):
        print(f"Found existing output directory. \nCleaning now...")
        shutil.rmtree(full_path)
        os.mkdir(full_path)
    else:
        print(f"{full_path} not found. Creating new one...")
        os.mkdir(full_path)


def copy_assets(src, dest):
    print(f"Copying {src} to {dest}")
    for file in os.listdir(src):
        full_path = os.path.join(src, file)
        if os.path.isfile(full_path):
            print(f"Copying file {file}...")
            shutil.copy(full_path, os.path.join(dest, file))
        elif os.path.isdir(full_path):
            print(f"Copying files from {file}")
            os.mkdir(os.path.join(dest, file))
            copy_assets(os.path.join(src, file), os.path.join(dest, file))


if __name__ == "__main__":
    clean_output_dir()
    copy_assets(INPUT_DIR, OUTPUT_DIR)
    from_path = os.path.join(os.getcwd(), "content")
    dest_path = os.path.join(os.getcwd(), "public")
    template = os.path.join(from_path, "template.html")
    generate_pages_recursive(from_path, template, dest_path)
