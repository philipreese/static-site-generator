import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()