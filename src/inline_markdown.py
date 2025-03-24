import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    split_nodes = []
    sections = old_node.text.split(delimiter)

    if len(sections) % 2 == 0:
      raise ValueError("invalid markdown, formatted section not closed")
    
    for i in range(len(sections)):
      if sections[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(sections[i], TextType.TEXT))
      else:
        split_nodes.append(TextNode(sections[i], text_type))
        
    new_nodes.extend(split_nodes)

  return new_nodes

def extract_markdown_images(text):
  return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
  return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
  return __split_nodes(old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes):
  return __split_nodes(old_nodes, TextType.LINK)

def __split_nodes(old_nodes, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    split_nodes = []
    sections = extract_markdown_links(old_node.text)

    if sections == None:
      new_nodes.append([])
      continue
    
    extra_markdown_for_image = "!" if text_type == TextType.IMAGE else ""

    split_text = old_node.text
    for anchor_text, url in sections:
      split = split_text.split(f"{extra_markdown_for_image}[{anchor_text}]({url})", 1)
      if len(split) != 2:
        raise ValueError("invalid markdown, link section not closed")
      
      if split[0] != "":
        split_nodes.append(TextNode(split[0], TextType.TEXT))

      split_nodes.append(TextNode(anchor_text, text_type, url))
      split_text = split[1]
    
    if split_text != "":
      split_nodes.append(TextNode(split_text, TextType.TEXT))
    new_nodes.extend(split_nodes)

  return new_nodes