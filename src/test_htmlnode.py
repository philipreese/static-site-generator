import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
      node = HTMLNode()
      node2 = HTMLNode()
      self.assertEqual(node, node2)

    def test_neq(self):
      node = HTMLNode("tag1")
      node2 = HTMLNode("tag2")
      self.assertNotEqual(node, node2)
      
    def test_props_to_html(self):
      props = {
        "href": "https://www.google.com",
        "target": "_blank",
      }
      expected = ' href="https://www.google.com" target="_blank"'
      node = HTMLNode(props=props)
      actual = node.props_to_html()
      self.assertEqual(actual, expected)
    
    def test_leaf_to_html_p(self):
      node = LeafNode("p", "Hello, world!")
      self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
      node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
      self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_image(self):
      node = LeafNode("h1", "Hello, world!")
      self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

if __name__ == "__main__":
    unittest.main()