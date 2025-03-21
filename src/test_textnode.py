import unittest

from textnode import TextNode, TextType, text_node_to_html_node
       
class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_eq_url(self):
    node = TextNode("This is a text node", TextType.BOLD, "url1")
    node2 = TextNode("This is a text node", TextType.BOLD, "url1")
    self.assertEqual(node, node2)

  def test_neq_text(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a test node", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_neq_text_type(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.LINK)
    self.assertNotEqual(node, node2)

  def test_neq_url_none(self):
    node = TextNode("This is a text node", TextType.BOLD, None)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
      
  def test_neq_url_given(self):
    node = TextNode("This is a text node", TextType.BOLD, "url1")
    node2 = TextNode("This is a text node", TextType.BOLD, "url2")
    self.assertNotEqual(node, node2)

  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_bold(self):
    node = TextNode("This is a bold node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")
    
  def test_italic(self):
    node = TextNode("This is an italic node", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")
    
  def test_code(self):
    node = TextNode("This is a code node", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")
    
  def test_link(self):
    node = TextNode("This is a link node", TextType.LINK, "test.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    print(html_node.to_html())
    self.assertEqual(html_node.to_html(), '<a href="test.com">This is a link node</a>')
    
  def test_image(self):
    node = TextNode("This is an image node", TextType.IMAGE, "test.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.to_html(), '<img src="test.com" alt="This is an image node"></img>')

if __name__ == "__main__":
    unittest.main()