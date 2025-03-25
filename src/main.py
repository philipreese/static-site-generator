import os
import shutil
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    recursive_copy(dir_path_static, dir_path_public)


def recursive_copy(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        for item in os.listdir(destination_dir):
            item_path = os.path.join(destination_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

    for item in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item)
        destination_item_path = os.path.join(destination_dir, item)

        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, destination_item_path)
        elif os.path.isdir(source_item_path):
            if not os.path.exists(destination_item_path):
                os.mkdir(destination_item_path)
            recursive_copy(source_item_path, destination_item_path)


main()
