import sys
from webpage import generate_pages_recursive, recursive_copy

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    recursive_copy(dir_path_static, dir_path_docs)
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_docs)


main()
