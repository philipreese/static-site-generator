import os
import shutil

from block_markdown import markdown_to_html_node


def recursive_copy(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        for item in os.listdir(destination_dir):
            item_path = os.path.join(destination_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    else:
        os.mkdir(destination_dir)

    for item in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item)
        destination_item_path = os.path.join(destination_dir, item)

        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, destination_item_path)
        elif os.path.isdir(source_item_path):
            if not os.path.exists(destination_item_path):
                os.mkdir(destination_item_path)
            recursive_copy(source_item_path, destination_item_path)


def extract_title(markdown):
    h1_node = markdown_to_html_node(markdown).children[0]
    if h1_node.tag != "h1":
        raise Exception("expecting h1 at beginning of markdown")
    return h1_node.children[0].value


def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f_p:
        markdown_content = f_p.read()
    with open(template_path) as t_p:
        template_text = t_p.read()

    title = extract_title(markdown_content)
    html_text = markdown_to_html_node(markdown_content).to_html()
    replaced_text = template_text.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_text
    )
    replaced_text = replaced_text.replace('href="/', f"href='{basepath}")
    replaced_text = replaced_text.replace('src="/', f"href='{basepath}")

    dest_path_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_path_dir):
        os.mkdir(dest_path_dir)

    with open(dest_path, mode="w") as d_p:
        d_p.write(replaced_text)


def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        source_item_path = os.path.join(dir_path_content, item)
        destination_item_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(source_item_path):
            dest_file = os.path.splitext(destination_item_path)[0] + ".html"
            generate_page(basepath, source_item_path, template_path, dest_file)
        elif os.path.isdir(source_item_path):
            if not os.path.exists(destination_item_path):
                os.mkdir(destination_item_path)
            generate_pages_recursive(
                basepath, source_item_path, template_path, destination_item_path
            )
