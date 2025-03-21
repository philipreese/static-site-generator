from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
  textNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  print(textNode)
  htmlNode = HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
  })
  print(htmlNode)
  print(htmlNode.props_to_html())

main()