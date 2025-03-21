class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    if self.props is None:
      return ""
    return "".join(map(lambda x: f' {x}="{self.props[x]}"', self.props))
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
  def __eq__(self, other):
    return (
      self.tag == other.tag and
      self.value == other.value and
      self.children == other.children and
      self.props == other.props
    )

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("invalid HTML: no value")
    
    if self.tag is None:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"