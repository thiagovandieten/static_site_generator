import unittest
from src.textnode import TextType, TextNode
from src.leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a Bold text node", TextType.BOLD)
        node2 = TextNode("This is a Italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_urls(self):
        node = TextNode("I'm an url!", TextType.LINK, "https://code.dev")
        node2 = TextNode("I'm an url!", TextType.LINK, "https://code.dev")
        self.assertEqual(node, node2)

    def test_normal_text_to_node(self):
        node = TextNode("I'm just text!", TextType.NORMAL)
        self.assertEqual(node.to_leafNode(), LeafNode("I'm just text!"))

    def test_bold_text_to_node(self):
        node = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(node.to_leafNode(), LeafNode("Bold text", "b"))

    def test_italic_text_to_node(self):
        node = TextNode("Italic text", TextType.ITALIC)
        self.assertEqual(node.to_leafNode(), LeafNode("Italic text", "i"))

    def test_code_text_to_node(self):
        node = TextNode("Code text", TextType.CODE)
        self.assertEqual(node.to_leafNode(), LeafNode("Code text", "code"))

    def test_link_text_to_node(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node.to_leafNode(), LeafNode("Link text", "a", {"href": "https://example.com"}))

    def test_image_text_to_node(self):
        node = TextNode("Image text", TextType.IMAGE, "https://example.com/image.png")
        self.assertEqual(node.to_leafNode(), LeafNode("Image text", "img", {"src": "https://example.com/image.png"}))


if __name__ == "__main__":
    unittest.main()
