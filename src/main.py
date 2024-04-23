import os
import shutil

OUTPUT_DIR = "public"


def clean_output_dir():
    print("Cleaning out dir...")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, "..", "public")
    print(f"{full_path} exists. Cleaning now...")

    # shutil.rmtree(os.path.)


def copy_static_assets():
    print("Copying static assets")


if __name__ == "__main__":
    clean_output_dir()
    copy_static_assets()
